# Create your models here.
"""
    数据库表模型类
"""
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone as timezone
'''
# 定义用户表user
class user(models.Model):
    UID = models.CharField(default=CALLABLE_FUNC, verbose_name='ID', primary_key=True,) #置为随机数函数
    UName = models.CharField(default=0, max_length=20, verbose_name='用户名')
    UPassword = models.CharField(default=0, max_length=32, verbose_name='密码')
#    UPicture = models.CharField(default=0, max_length=20, verbose_name='用户头像')
    image = models.ImageField(default="images/0.jpg", upload_to="images/", verbose_name='头像')
#    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'user'  # 指明数据库表名
        verbose_name = '用户'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.user
'''
class UserProfile(AbstractUser):
    # mobile = models.CharField(max_length=11, verbose_name="手机号", unique=True)

    # upload_to表示文件上传的路径，uploads/%Y/%m/%d：会在media文件底下依次创建2019--05--文件名
    # image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    # media创建在static同级目录下
    image = models.ImageField(default="static/images/0.jpg", upload_to="static/images/")
    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

class topic(models.Model):
    TID = models.AutoField(verbose_name='TID', primary_key=True,)
    UID_id = models.IntegerField(default=0, verbose_name="发帖用户id")
    TReplyCount = models.IntegerField(default=0, verbose_name="回帖数")
    TLastClickT = models.DateTimeField(auto_now=True, verbose_name="最后回复时间")
    TTopic = models.CharField(max_length=200, default=0, verbose_name="贴标题")
    TContent = models.TextField(default=0, verbose_name="贴内容")
    TPicture = models.ImageField(null=True, upload_to="../media/", verbose_name="贴图片")
    TTime = models.DateTimeField(auto_now_add=True, verbose_name="发帖时间")
    username = models.CharField(max_length=150, default='雪鸮', verbose_name='发帖用户名')
    class Meta:
        db_table = 'topic'
        verbose_name = '主帖表'
        verbose_name_plural = verbose_name
        ordering = ['-TTime'] # 查询的数据按指定字段排序

class reply(models.Model):
    RID = models.AutoField(verbose_name='RID', primary_key=True, )
    TID = models.IntegerField(default=0, verbose_name="主贴id")
    UID_id = models.IntegerField(default=0, verbose_name="发帖用户id")
    RContent = models.TextField(default=0, verbose_name="贴内容")
    RPicture = models.ImageField(null=True, upload_to="../media/", verbose_name="回复贴图片")
    RTime = models.DateTimeField(auto_now_add=True, verbose_name="发帖时间")
    username = models.CharField(max_length=150, default='雪鸮', verbose_name='发帖用户名')
    class Meta:
        db_table = 'reply'
        verbose_name = '回复帖表'
        verbose_name_plural = verbose_name

class prtopic(models.Model):
    TID = models.AutoField(verbose_name='TID', primary_key=True,)
    UID_id = models.IntegerField(default=0, verbose_name="发帖用户id")
    reid = models.IntegerField(null=True, verbose_name="指定阅读用户的id")
    TTopic = models.CharField(max_length=200, default=0, verbose_name="隐私贴标题")
    TContent = models.TextField(default=0, verbose_name="隐私贴内容")
    TPicture = models.ImageField(null=True, upload_to="../media/", verbose_name="隐私贴图片")
    TTime = models.DateTimeField(auto_now_add=True, verbose_name="发帖时间")
    username = models.CharField(max_length=150, default='雪鸮', verbose_name='发帖用户名')
    class Meta:
        db_table = 'prtopic'
        verbose_name = '隐私帖表'
        verbose_name_plural = verbose_name

