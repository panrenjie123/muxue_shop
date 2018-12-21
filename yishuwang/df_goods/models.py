from django.db import models
from df_user.models import University,Career,College
from tinymce.models import HTMLField
from df_user.models import UserInfo
from datetime import datetime
# Create your models here.

class TypesInfo(models.Model):
    type_name = models.CharField(max_length=30,verbose_name='类名')
    parent = models.ForeignKey('self',null=True,blank=True)
    def __str__(self):
        return self.type_name
    class Meta:
        verbose_name = '分类表'
        verbose_name_plural = verbose_name

class Grade(models.Model):
    title = models.CharField(max_length=30,verbose_name='年级名称')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '年级表'
        verbose_name_plural = verbose_name

class BookInfo(models.Model):
    bookname = models.CharField(max_length=50,verbose_name='书名')
    picture = models.ImageField(upload_to='books',verbose_name='图片')
    price = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='价格')
    number = models.IntegerField(verbose_name='库存',default=100)
    university = models.ForeignKey(University,verbose_name='大学')
    college = models.ForeignKey(College,verbose_name='学院')
    career = models.ForeignKey(Career,verbose_name='专业')
    grade = models.ForeignKey(Grade,verbose_name='年级')
    types = models.ForeignKey(TypesInfo,verbose_name='分类')
    share_book = models.ForeignKey(UserInfo,verbose_name='分享用户',null=True,blank=True)
    publish_date = models.DateTimeField(default=datetime.now,verbose_name='发布时间')
    desc = HTMLField(verbose_name='描述')
    def __str__(self):
        return self.bookname
    class Meta:
        verbose_name = '图书表'
        verbose_name_plural = verbose_name
