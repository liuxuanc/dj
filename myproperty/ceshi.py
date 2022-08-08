from mycelery.main import app
from celery.result import AsyncResult

id = '75cd4ecb-f135-4c8c-bf66-ae026918b988'


my_async = AsyncResult(id=id, app=app)
if my_async.successful():
    result = my_async.get()
    print(result)
elif my_async.failed():
    print('failed')
elif my_async.status == 'PENDING':
    print('PENDING')
elif my_async.status == 'RETRY':
    print('RETRY')
elif my_async.status == 'STARTED':
    print('STARTED')


