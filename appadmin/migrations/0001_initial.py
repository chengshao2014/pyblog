# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 03:08
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_manager_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_account', models.CharField(max_length=64, verbose_name='管理员帐号')),
                ('admin_passwd', models.CharField(max_length=128, verbose_name='管理员登录密码')),
                ('admin_auth_token', models.CharField(max_length=128, verbose_name='验证token')),
                ('registered_time', models.DateTimeField(default=datetime.datetime(2016, 12, 14, 3, 8, 58, 580090, tzinfo=utc), verbose_name='注册时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'ordering': ['-update_time'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('body', models.TextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=1, verbose_name='文章状态')),
                ('abstract', models.CharField(blank=True, help_text='可选，如若为空将摘取正文的前54个字符', max_length=54, null=True, verbose_name='摘要')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('topped', models.BooleanField(default=False, verbose_name='置顶')),
            ],
            options={
                'ordering': ['-last_modified_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20, verbose_name='类名')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=datetime.datetime(2016, 12, 14, 3, 8, 58, 578591, tzinfo=utc))),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appadmin.Category', verbose_name='分类'),
        ),
    ]
