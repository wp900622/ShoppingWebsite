from django.db import models

# Create your models here.
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    first = models.CharField('一級類型',max_length=100)
    second = models.CharField('二級類型',max_length=100)
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '商品類型'
        verbose_name_plural = '商品類型'

class CommodityInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('商品名稱',max_length=100)
    size = models.CharField('顏色規格',max_length=100)
    type = models.CharField('商品類型',max_length=100)
    price = models.FloatField('商品價格')
    discount = models.FloatField('折價後價格')
    stock = models.IntegerField('存貨數量')
    sold = models.IntegerField('已售數量')
    likes = models.IntegerField('收藏數量')
    created = models.DateTimeField('上架日期', auto_now_add=True)
    img = models.FileField('商品目錄', upload_to=r'img')
    details = models.FileField('商品介紹', upload_to=r'details')
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'
