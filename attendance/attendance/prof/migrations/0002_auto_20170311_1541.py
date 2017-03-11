# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='attendance',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
    ]
