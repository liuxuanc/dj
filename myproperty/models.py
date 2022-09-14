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
    # add_time = models.DateTimeField(blank=True, default='', verbose_name='添加时间', null=True)
    add_time = models.DateTimeField(blank=True, null=True, default=None, verbose_name='添加时间')
    asset_code = models.CharField(max_length=32, verbose_name='资产编码', blank=False, null=False)
    current_user = models.CharField(max_length=8, verbose_name='使用者', null=True)
    requisition_time = models.DateTimeField(blank=True, null=True, default=None, verbose_name='领用日期')
    # requisition_time = models.DateTimeField(blank=True, null=True, default=timezone.now, verbose_name='领用日期')
    user_one = models.CharField(max_length=8, verbose_name='使用者1', default=None, null=True)
    user_one_requisition_time = models.DateTimeField(blank=True, null=True, default=None, verbose_name='使用者1领用日期')
    return_date = models.DateTimeField(blank=True, null=True, verbose_name='归还日期', default=None)
    remarks = models.TextField(verbose_name='备注', null=True, default=None)
    sn = models.CharField(max_length=32, verbose_name='sn号', null=True)
    parameter = models.TextField(verbose_name='具体参数', null=True)
    # alter_time = models.DateTimeField(verbose_name='修改日期', default=timezone.now, null=True)

    class Meta:
        verbose_name = '资产表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pro_name


class Grant(models.Model):
    info_code = models.CharField(max_length=32, verbose_name='资产编码', blank=False, null=False)
    info = models.ForeignKey(Info, on_delete=models.CASCADE, default='')
    alters_date = models.DateTimeField(blank=True, verbose_name='时间', null=True)
    signature = models.ImageField(max_length=255, upload_to='signature/', verbose_name=u'签名', null=True, blank=True)
    device = models.CharField(max_length=32, verbose_name='设备名', blank=True, null=True)
    specification = models.CharField(max_length=32, verbose_name='规格型号', blank=True, null=True)
    user_name = models.CharField(max_length=8, verbose_name='使用人', blank=True, null=True)
    sn_num = models.CharField(max_length=16, verbose_name='sn', blank=True, null=True)

    class Meta:
        db_table = 'Grant'
        verbose_name = '签名'
        verbose_name_plural = verbose_name

