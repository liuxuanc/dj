# Generated by Django 3.2 on 2022-07-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproperty', '0012_alter_grant_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='signature',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='signature/', verbose_name='签名'),
        ),
    ]
