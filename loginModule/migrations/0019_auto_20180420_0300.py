# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-19 21:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginModule', '0018_auto_20180420_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillsDescriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wood', models.CharField(max_length=20)),
                ('rate', models.IntegerField(max_length=10)),
                ('volume', models.IntegerField(max_length=10)),
                ('last_updated_time', models.DateTimeField(default=datetime.datetime(2018, 4, 20, 3, 0, 25, 313938))),
            ],
        ),
        migrations.RemoveField(
            model_name='billdescriptions',
            name='bill_id',
        ),
        migrations.AlterField(
            model_name='bills',
            name='last_updated_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 20, 3, 0, 25, 312938)),
        ),
        migrations.AlterField(
            model_name='clientdetail',
            name='last_updated_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 20, 3, 0, 25, 311938)),
        ),
        migrations.DeleteModel(
            name='BillDescriptions',
        ),
        migrations.AddField(
            model_name='billsdescriptions',
            name='bill_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginModule.Bills'),
        ),
    ]
