依赖pyhessian，bitstring

示例代码
::

    from dubbo import DubboConsumer


    def print_hi(consumer):
        req = consumer.queryCusStatis([("Lcom/weimob/o2o/wecom/data/api/interfaces/query/request/CusStatisRequest;",
                                        {"corpid": 1, "dateRangeType": 3})])
        print(f'req: {req!r}')
        for dto in req.responseVo.data.cusStatisDayDtos:
            print(f'dto: {dto!r}')


    if __name__ == '__main__':
        consumer = DubboConsumer("10.11.32.251:2181", "com.weimob.o2o.wecom.data.api.interfaces.query.QueryCusApi")
        print_hi(consumer)





具体参照测main.py，目前支持常用的dubbo协议。