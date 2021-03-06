# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-12 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loginModule', '0024_auto_20180426_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierWoodDescriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wood', models.CharField(max_length=20)),
                ('wood_code', models.CharField(default='', max_length=40)),
                ('rate', models.FloatField(default=0, max_length=50)),
                ('volume', models.FloatField(default=0, max_length=50)),
                ('total', models.FloatField(default=0, max_length=50)),
                ('gst_tax', models.FloatField(default=0, max_length=2)),
                ('last_updated_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='billsdescriptions',
            name='gst_tax',
            field=models.FloatField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='billsdescriptions',
            name='total',
            field=models.FloatField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='billsdescriptions',
            name='wood_code',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='supplierdetail',
            name='sender_phone',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='bills',
            name='last_updated_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='billsdescriptions',
            name='last_updated_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='clientdetail',
            name='client_phone',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='clientdetail',
            name='last_updated_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='supplierdetail',
            name='tax_type',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='supplierwooddescriptions',
            name='invoice_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginModule.SupplierDetail'),
        ),
    ]
