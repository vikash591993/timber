# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginModule', '0007_auto_20180410_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vikash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
