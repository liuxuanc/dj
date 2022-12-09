# Generated by Django 3.2 on 2022-08-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproperty', '0018_alter_info_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='add_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='info',
            name='requisition_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='领用日期'),
        ),
        migrations.AlterField(
            model_name='info',
            name='return_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='归还日期'),
        ),
        migrations.AlterField(
            model_name='info',
            name='user_one',
            field=models.CharField(default=None, max_length=8, null=True, verbose_name='使用者1'),
        ),
        migrations.AlterField(
            model_name='info',
            name='user_one_requisition_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='使用者1领用日期'),
        ),
    ]