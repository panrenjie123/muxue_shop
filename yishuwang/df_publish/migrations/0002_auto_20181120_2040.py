# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-20 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_publish', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='订单号'),
        ),
    ]
