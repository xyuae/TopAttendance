# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0003_merge_20170311_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Indicator',
            name='class_code',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]