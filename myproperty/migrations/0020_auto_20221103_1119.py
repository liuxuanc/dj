# Generated by Django 3.2 on 2022-11-03 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproperty', '0019_auto_20220817_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info',
            options={'permissions': (('Info_select', '常用任务查看权限'), ('Info_change', '常用任务修改权限'), ('Info_run', '执行常用任务')), 'verbose_name': '资产表', 'verbose_name_plural': '资产表'},
        ),
        migrations.RemoveField(
            model_name='info',
            name='parameter',
        ),
    ]
