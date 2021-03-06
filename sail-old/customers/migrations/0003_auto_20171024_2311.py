# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-24 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20171024_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customertransgoodsinfo',
            name='customer_trans_info',
        ),
        migrations.RemoveField(
            model_name='customertransinfo',
            name='customer',
        ),
        migrations.AddField(
            model_name='transinfo',
            name='trans_payment_float',
            field=models.FloatField(blank=True, default=0, verbose_name='总货款'),
        ),
        migrations.AddField(
            model_name='transinfo',
            name='trans_reduction_float',
            field=models.FloatField(blank=True, default=0, verbose_name='优惠'),
        ),
        migrations.DeleteModel(
            name='CustomerTransGoodsInfo',
        ),
        migrations.DeleteModel(
            name='CustomerTransInfo',
        ),
    ]
