from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=100,verbose_name='公告名')
    create_time = models.DateTimeField(default=datetime.now,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='最新更新时间')
    browers_number = models.IntegerField(default=0,verbose_name='浏览量')
    desc = HTMLField(verbose_name='简介')
    intro = HTMLField(verbose_name='介绍')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '公告表'
        verbose_name_plural = verbose_name














