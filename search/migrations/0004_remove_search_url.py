# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 17:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_result_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='url',
        ),
    ]
