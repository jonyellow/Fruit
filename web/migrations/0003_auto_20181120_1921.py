# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-20 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20181120_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='tel',
            field=models.BigIntegerField(max_length=11, verbose_name='电话号码'),
        ),
    ]