# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-19 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=20, verbose_name='姓名')),
                ('address_text', models.CharField(blank=True, max_length=100, verbose_name='地址')),
                ('mobile1_text', models.CharField(blank=True, max_length=30, verbose_name='工作手机号码')),
                ('mobile2_text', models.CharField(blank=True, max_length=30, verbose_name='家庭手机号码')),
                ('phone1_text', models.CharField(blank=True, max_length=30, verbose_name='固定电话')),
                ('phone2_text', models.CharField(blank=True, max_length=30, verbose_name='固定电话2')),
                ('email', models.CharField(blank=True, max_length=30, verbose_name='Email')),
                ('comment', models.CharField(blank=True, max_length=1000, verbose_name='备注')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加日期')),
            ],
            options={
                'verbose_name': '联系人信息',
                'verbose_name_plural': '联系人信息',
            },
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='费用名称')),
                ('price', models.FloatField(default=0, verbose_name='价格')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加日期')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='公司名称')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='地址')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加日期')),
                ('invoice', models.CharField(blank=True, max_length=50, verbose_name='发票抬头')),
                ('comment', models.CharField(blank=True, max_length=1000, verbose_name='备注')),
                ('contacts', models.ManyToManyField(blank=True, related_name='customer_company', to='customers.Contact', verbose_name='联系人')),
            ],
            options={
                'verbose_name': '客户信息',
                'verbose_name_plural': '客户信息',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('price', models.FloatField(default=0, verbose_name='单价')),
                ('buying_price', models.FloatField(default=0, verbose_name='进货价')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加日期')),
                ('comment', models.CharField(blank=True, max_length=1000, verbose_name='备注')),
            ],
            options={
                'verbose_name': '货物信息',
                'verbose_name_plural': '货物信息',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='名称')),
                ('picture', models.ImageField(blank=True, upload_to='images', verbose_name='图片')),
                ('comment', models.CharField(blank=True, max_length=1000, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='公司名称')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='地址')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加日期')),
                ('comment', models.CharField(blank=True, max_length=1000, verbose_name='备注')),
                ('contacts', models.ManyToManyField(blank=True, related_name='provider_company', to='customers.Contact', verbose_name='联系人')),
            ],
        ),
        migrations.CreateModel(
            name='Trans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled_key', models.IntegerField(default=0)),
                ('trans_name_text', models.CharField(max_length=100, verbose_name='交易名称')),
                ('trans_order_number_text', models.CharField(blank=True, max_length=100, verbose_name='订单号')),
                ('contract_name_text', models.CharField(max_length=100, verbose_name='合同编号')),
                ('trans_fax_int', models.IntegerField(blank=True, default=0, verbose_name='税点')),
                ('trans_payment_float', models.FloatField(blank=True, default=0, verbose_name='总货款')),
                ('trans_reduction_float', models.FloatField(blank=True, default=0, verbose_name='优惠')),
                ('trans_date', models.DateField(blank=True, null=True, verbose_name='交易日期')),
                ('goods_delivery_date', models.DateField(blank=True, null=True, verbose_name='交货日期')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加日期')),
                ('comment_text', models.CharField(blank=True, max_length=1000, verbose_name='备注')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trans', to='customers.Contact', verbose_name='联系人')),
                ('costs', models.ManyToManyField(blank=True, related_name='trans', to='customers.Cost', verbose_name='费用')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trans', to='customers.Customer', verbose_name='公司')),
            ],
            options={
                'verbose_name': '交易信息',
                'verbose_name_plural': '交易信息',
            },
        ),
        migrations.CreateModel(
            name='TransGoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled_key', models.IntegerField(default=0)),
                ('num_int', models.IntegerField(default=0, verbose_name='数量')),
                ('price_float', models.FloatField(default=0, verbose_name='成交单价')),
                ('price_quoted_float', models.FloatField(default=0, verbose_name='报价')),
                ('goods_color_text', models.CharField(max_length=100, verbose_name='颜色')),
                ('comment_text', models.CharField(blank=True, max_length=1000, verbose_name='备注')),
                ('costs', models.ManyToManyField(blank=True, related_name='trans_goods', to='customers.Cost', verbose_name='费用')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trans_goods', to='customers.Goods', verbose_name='货物')),
                ('pictures', models.ManyToManyField(blank=True, related_name='trans_goods', to='customers.Picture', verbose_name='图片')),
                ('trans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trans_goods', to='customers.Trans', verbose_name='交易')),
            ],
            options={
                'verbose_name': '交易货物信息',
                'verbose_name_plural': '交易货物信息',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='pictures',
            field=models.ManyToManyField(blank=True, related_name='goods', to='customers.Picture', verbose_name='图片'),
        ),
        migrations.AddField(
            model_name='goods',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='customers.Provider', verbose_name='图片'),
        ),
    ]
