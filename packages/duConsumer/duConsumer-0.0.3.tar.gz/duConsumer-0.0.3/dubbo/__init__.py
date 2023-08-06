# -*- coding: utf-8 -*-
from urllib.parse import urlparse, unquote, parse_qs

from socket import socket, AF_INET, SOCK_STREAM

from bitstring import BitStream
from kazoo.client import KazooClient

import threading

from utils import encoder, parser


class Attachments(dict):
    def __setattr__(self, k, v):
        self[k] = v

    def __getattr__(self, k):
        return self[k]


class ResponseCode:
    RESPONSE_WITH_EXCEPTION = 144
    RESPONSE_VALUE = 145
    RESPONSE_NULL_VALUE = 146
    RESPONSE_WITH_EXCEPTION_WITH_ATTACHMENTS = 147
    RESPONSE_VALUE_WITH_ATTACHMENTS = 148
    RESPONSE_NULL_VALUE_WITH_ATTACHMENTS = 149


class DubboConsumer(object):
    _instance_lock = threading.Lock()

    def __init__(self, hosts, interface, version="0.0.0", dubbo_v="2.6.8"):
        self._rr = 0
        self.dubbo_v = dubbo_v
        self.interface = interface
        self.version = version
        self.method = None
        self.args = None
        self.attachments = None
        # zk
        self.zk = KazooClient(hosts=hosts)
        self.zk.start()
        # providers
        providers = self.zk.get_children("/dubbo/%s/providers" % interface)
        uris = [urlparse(unquote(provider)) for provider in providers]
        self.uris = uris

        if len(uris) == 0:
            print("no service found")
            exit(-1)

        # client
        clients = []
        for uri in uris:
            client = socket(AF_INET, SOCK_STREAM)
            client.connect((uri.hostname, uri.port))
            clients.append(client)
        self.clients = clients

        # add method
        query = None
        if "methods" in uris[0].path:
            query = uris[0].path
        elif "methods" in uris[0].query:
            query = uris[0].query
        else:
            print("no method found.")
            exit(-2)

        if query is not None:
            params = parse_qs(query)
            for method in params["methods"][0].split(","):
                def _decorator(func):
                    def _(*args):
                        self.method = func
                        self.args = args[0]
                        return self.invoke(*args)

                    return _

                setattr(self, method, _decorator(method))

    def __new__(cls, *args, **kwargs):
        if not hasattr(DubboConsumer, "_instance"):
            with DubboConsumer._instance_lock:
                if not hasattr(DubboConsumer, "_instance"):
                    DubboConsumer._instance = object.__new__(cls)
        return DubboConsumer._instance

    def _encode(self, encoder):
        elements = bytearray()
        elements.extend(encoder.encode(self.dubbo_v))
        elements.extend(encoder.encode(self.interface))
        if self.version:
            elements.extend(encoder.encode(self.version))
        elements.extend(encoder.encode(self.method))

        arg_type = "".join([arg_type for arg_type, _ in self.args])
        elements.extend(encoder.encode(arg_type))
        for _, arg in self.args:
            elements.extend(encoder.encode(arg))
        self.attachments = self.attachments if self.attachments else Attachments(
            {"path": self.interface, "interface": self.interface, 'version': self.version})
        elements.extend(encoder.encode(self.attachments))

        return elements

    def _invoke(self, client):
        request_body = self._encode(encoder.Encoder())
        dubbo_request_body = BitStream(
            f'intbe:16=-9541,intbe:8=-62,intbe:8=0,uintbe:64=0,uintbe:32={len(request_body)}')
        dubbo_request_body.append(request_body)
        client.send(dubbo_request_body.bytes)

        dubbo_response_length = \
            BitStream(bytes=client.recv(16)).readlist('intbe:16,intbe:8,intbe:8,uintbe:64,uintbe:32')[-1]

        dubbo_response_body = BitStream()
        while dubbo_response_length - len(dubbo_response_body) / 8 > 0:
            dubbo_response_body.append(client.recv(1024))

        code = dubbo_response_body.read('uintbe:8')
        if code in (ResponseCode.RESPONSE_NULL_VALUE, ResponseCode.RESPONSE_NULL_VALUE_WITH_ATTACHMENTS):
            return None
        elif code in (ResponseCode.RESPONSE_WITH_EXCEPTION, ResponseCode.RESPONSE_WITH_EXCEPTION_WITH_ATTACHMENTS):
            p = parser.ParserV2(dubbo_response_body)
            res = p.read_object()
            raise Exception(res)
        elif code in (ResponseCode.RESPONSE_VALUE, ResponseCode.RESPONSE_VALUE_WITH_ATTACHMENTS):
            p = parser.ParserV2(dubbo_response_body)
            res = p.read_object()
            return res
        else:
            raise Exception(f"code={code}")

    def invoke(self, *args):
        if len(args) > 1:
            self.method = args[0]
            self.args = args[1]

        clients_len = len(self.clients)
        self._rr = (self._rr + 1) % clients_len
        return self._invoke(self.clients[self._rr])

    def close(self):
        for client in self.clients:
            try:
                client.close()
            except Exception as e:
                print(e)
