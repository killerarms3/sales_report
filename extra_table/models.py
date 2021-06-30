from django.db import models

# Create your models here.
class Stores(models.Model):
    code = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    category = models.CharField(max_length=256, blank=True, null=True)
    subtype = models.CharField(max_length=256, blank=True, null=True)

class SKU(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    sku = models.CharField(max_length=256, blank=True, null=True)
    cost = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=256, blank=True, null=True)

class Store_house(models.Model):
    code = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    category = models.CharField(max_length=256, blank=True, null=True)
    subtype = models.CharField(max_length=256, blank=True, null=True)


class CRM_tags(models.Model):
    tag = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    subtype = models.CharField(max_length=256)