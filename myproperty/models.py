from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Info(models.Model):
    id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=8,verbose_name='姓名', default='')
    # gender = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别')
    pro_name = models.CharField(max_length=32, verbose_name='资产名称', blank=False, null=False)
    type = models.TextField(verbose_name='规格型号', blank=False, null=False)
    num = models.IntegerField(verbose_name='数量', blank=False, null=False)
    add_time = models.DateTimeField(blank=True, default='', verbose_name='添加时间', null=True)
    asset_code = models.CharField(max_length=32, verbose_name='资产编码', blank=False, null=False)
    current_user = models.CharField(max_length=8, verbose_name='使用者', null=True)
    requisition_time = models.DateTimeField(blank=True, null=True, default='', verbose_name='领用日期')
    user_one = models.CharField(max_length=8, verbose_name='使用者1', default='', null=True)
    user_one_requisition_time = models.DateTimeField(blank=True, null=True, default='', verbose_name='使用者1领用日期')
    return_date = models.DateTimeField(blank=True, null=True, verbose_name='归还日期', default='')
    remarks = models.TextField(verbose_name='备注', null=True, default=None)
    # alter_time = models.DateTimeField(verbose_name='修改日期', default=timezone.now, null=True)
