# Generated by Django 3.2 on 2022-06-08 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pro_name', models.CharField(blank=True, max_length=32, verbose_name='资产名称')),
                ('type', models.TextField(verbose_name='规格型号')),
                ('num', models.IntegerField(null=True, verbose_name='数量')),
                ('add_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='添加时间')),
                ('asset_code', models.CharField(blank=True, max_length=32, verbose_name='资产编码')),
                ('current_user', models.CharField(max_length=8, null=True, verbose_name='使用者')),
                ('requisition_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='领用日期')),
                ('user_one', models.CharField(default='', max_length=8, null=True, verbose_name='使用者1')),
                ('user_one_requisition_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='使用者1领用日期')),
                ('return_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='归还日期')),
                ('remarks', models.TextField(default=None, null=True, verbose_name='备注')),
            ],
        ),
    ]