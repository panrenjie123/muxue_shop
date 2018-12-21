from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class University(models.Model):
    title = models.CharField(max_length=30,verbose_name='大学名称')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '大学表'
        verbose_name_plural = verbose_name

class College(models.Model):
    title = models.CharField(max_length=30,verbose_name='学院名称')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '学院表'
        verbose_name_plural = verbose_name

class Career(models.Model):
    title = models.CharField(max_length=30,verbose_name='专业名称')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '专业表'
        verbose_name_plural = verbose_name

class UserInfo(AbstractUser):
    nickname = models.CharField(max_length=30,verbose_name='昵称',default='')
    phone = models.CharField(max_length=11,verbose_name='手机号',default='')
    university = models.ForeignKey(University,verbose_name='大学',default=1)
    college = models.ForeignKey(College,verbose_name='学院',default=1)
    career = models.ForeignKey(Career,verbose_name='专业',default=1)
    grade = models.CharField(max_length=30,verbose_name='年级',default='')

