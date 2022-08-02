from datetime import timedelta
from celery.schedules import crontab

broker_url = 'redis://127.0.0.1:6379/1'

result_backend = 'redis://127.0.0.1:6379/2'

# CELERY_TIMEZONE = 'Asia/Shanghai'


# CELERYBEAT_SCHEDULE = {
#     # ÿ10sִ��һ��
#     'task1': {
#         'task': 'mycelery.task01.add',
#         'schedule': timedelta(seconds=10),
#         'args': (2, 8)
#     },
#     # ÿ��15:00ִ��
#     # 'task2': {
#     #     'task': 'celery_study.task_add.add',x`
#     #     'schedule': crontab(hour=15, minute=0),
#     #     'args': (9, 9)
#     # }
# }
