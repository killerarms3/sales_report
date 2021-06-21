from django.db import models

# Create your models here.
class Stores(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)

class SKU(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    sku = models.CharField(max_length=256, blank=True, null=True)
    cost = models.PositiveIntegerField(blank=True, null=True)