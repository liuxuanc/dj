# Generated by Django 3.2 on 2022-08-17 11:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myproperty', '0017_alter_info_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='add_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='添加时间'),
        ),
    ]
