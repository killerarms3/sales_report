from django.db import models

# Create your models here.
class Stores(models.Model):
    code = models.CharField(max_length=64, unique=True, verbose_name='店櫃代號')
    name = models.CharField(max_length=64, blank=True, null=True, verbose_name='店櫃名稱')
    category = models.CharField(max_length=64, verbose_name='大分類')
    subtype = models.CharField(max_length=64, verbose_name='小分類')
    class Meta:
        verbose_name = '店櫃名單'
        verbose_name_plural = '店櫃名單'

class SKU(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name='商品名稱')
    sku = models.CharField(max_length=64, unique=True, verbose_name='商品代號')
    cost = models.PositiveIntegerField(default=0, verbose_name='成本')
    status = models.CharField(max_length=64, blank=True, null=True, verbose_name='商品狀態')
    class Meta:
        verbose_name = '商品名單'
        verbose_name_plural = '商品名單'

class Store_house(models.Model):
    code = models.CharField(max_length=64, unique=True, verbose_name='倉庫代號')
    name = models.CharField(max_length=64, verbose_name='倉庫名稱')
    category = models.CharField(max_length=64, verbose_name='大分類')
    subtype = models.CharField(max_length=64, verbose_name='小分類')
    class Meta:
        verbose_name = '倉庫名單'
        verbose_name_plural = '倉庫名單'

class CRM_tags(models.Model):
    tag = models.CharField(max_length=256, verbose_name='標籤')
    category = models.CharField(max_length=64, verbose_name='大分類')
    subtype = models.CharField(max_length=64, verbose_name='小分類')
    class Meta:
        verbose_name = 'CRM標籤'
        verbose_name_plural = 'CRM標籤'