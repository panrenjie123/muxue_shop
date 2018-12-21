from django.db import models
from df_user.models import UserInfo
from df_goods.models import BookInfo
# Create your models here.


class Order(models.Model):
    order_status = (
        ("success", "已支付"),
        ("close", "超时关闭"),
        ("paying", "待支付"),
    )
    order_id = models.CharField(max_length=60,primary_key=True,verbose_name='订单号')
    user = models.ForeignKey(UserInfo,verbose_name='所属用户')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    isPay = models.BooleanField(default=False,verbose_name='是否支付')
    total = models.DecimalField(max_digits=6,decimal_places=2,verbose_name='总价')
    address = models.CharField(max_length=120,default='',verbose_name='地址')
    books = models.ForeignKey(BookInfo,verbose_name='书籍信息')
    count = models.IntegerField(default=1,verbose_name='书籍个数')
    pay_status = models.CharField(max_length=100, choices=order_status, default="paying", verbose_name="支付状态")
    def __str__(self):
        return self.order_id
    class Meta:
        verbose_name = '订单表'
        verbose_name_plural = verbose_name




