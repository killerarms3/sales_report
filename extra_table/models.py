from django.db import models

# Create your models here.
class Stores(models.Model):
    code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    category = models.CharField(max_length=64)
    subtype = models.CharField(max_length=64)

class SKU(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    sku = models.CharField(max_length=64, unique=True)
    cost = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=64, blank=True, null=True)

class Store_house(models.Model):
    code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    subtype = models.CharField(max_length=64)


class CRM_tags(models.Model):
    tag = models.CharField(max_length=256)
    category = models.CharField(max_length=64)
    subtype = models.CharField(max_length=64)
