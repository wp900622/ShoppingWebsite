from django.db import models

# Create your models here.
STATE = (
    ('待支付','待支付'),
    ('已支付', '已支付'),
    ('發貨中','發貨中'),
    ('已簽收','已簽收'),
    ('退貨中','退貨中')

)

class CartInfo(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField('購買數量')
    commodityinfos_id = models.IntegerField('商品Id')
    user_id = models.IntegerField('用戶id')

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name='購物車'
        verbose_name_plural='購物車'

class OrderInfo(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField('訂單總價')
    created = models.DateTimeField('創建時間', auto_now_add=True)
    user_id = models.IntegerField('用戶id')
    state = models.CharField('訂單狀態',max_length=20,choices=STATE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name='訂單信息'
        verbose_name_plural='訂單信息'
