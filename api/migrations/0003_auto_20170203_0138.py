# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170203_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
