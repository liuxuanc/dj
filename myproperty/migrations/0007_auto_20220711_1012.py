# Generated by Django 3.2 on 2022-07-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproperty', '0006_grant'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='parameter',
            field=models.TextField(null=True, verbose_name='具体参数'),
        ),
        migrations.AddField(
            model_name='info',
            name='sn',
            field=models.CharField(max_length=32, null=True, verbose_name='sn号'),
        ),
    ]
