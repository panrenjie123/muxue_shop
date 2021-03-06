# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-13 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=50, verbose_name='书名')),
                ('picture', models.ImageField(upload_to='books')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('desc', tinymce.models.HTMLField(verbose_name='描述')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.Career', verbose_name='专业')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.College', verbose_name='学院')),
            ],
            options={
                'verbose_name': '图书表',
                'verbose_name_plural': '图书表',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='年级名称')),
            ],
            options={
                'verbose_name': '年级表',
                'verbose_name_plural': '年级表',
            },
        ),
        migrations.CreateModel(
            name='TypesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=30, verbose_name='类名')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='df_goods.TypesInfo')),
            ],
            options={
                'verbose_name': '分类表',
                'verbose_name_plural': '分类表',
            },
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.Grade', verbose_name='年级'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.TypesInfo', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.University', verbose_name='大学'),
        ),
    ]
