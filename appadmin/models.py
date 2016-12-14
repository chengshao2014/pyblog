#coding:utf-8
#@author:AChan
#@Date : 2016/11/8 17:20
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250, unique_for_date = 'publish')
    author = models.ForeignKey(User, related_name = 'blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now())
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'draft')
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class admin_manager_info(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    admin_account = models.CharField('管理员帐号',max_length = 64)
    admin_passwd = models.CharField('管理员登录密码',max_length = 128)
    admin_auth_token = models.CharField('验证token',max_length = 128)
    registered_time = models.DateTimeField('注册时间',default = timezone.now())
    update_time = models.DateTimeField('更新时间',auto_now = True)
    # uid = models.AutoField()

    def __str__(self):
        return self.admin_account

    class Meta:
        ordering = ['-update_time']

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True,
                                help_text="可选，如若为空将摘取正文的前54个字符")
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)

    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']


class Category(models.Model):
    category_name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.category_name