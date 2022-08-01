# from mycelery.main import app
# from celery.result import AsyncResult
#
# id = '9a4f870a-b0aa-4c49-9520-53e855542446'
#
#
# my_async = AsyncResult(id=id, app=app)
# if my_async.successful():
#     result = my_async.get()
#     print(result)
# elif my_async.failed():
#     print('shibai')
# elif my_async.status == 'PENDING':
#     print('dengdai')
# elif my_async.status == 'RETRY':
#     print('yichang')
# elif my_async.status == 'STARTED':
#     print('zhengzai')
