# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginModule', '0006_auto_20180410_2341'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetail',
            new_name='UserName',
        ),
    ]
