import os
from djangoProject import settings

from celery import Celery


app = Celery('mycelery', broker='redis://127.0.0.1:6379/3')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app.config_from_object('mycelery.config')


app.autodiscover_tasks(["mycelery.wjw"])


