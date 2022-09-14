from django.apps import AppConfig


class MypropertyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myproperty'
    verbose_name = '资产信息'
