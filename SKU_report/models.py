from django.db import models
from extra_table.models import Stores, Store_house, SKU

# Create your models here.
class DailySalesBySKU(models.Model):
    date = models.DateField(blank=True, null=True)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    stores = models.ForeignKey(Stores, on_delete=models.CASCADE)
    counts = models.PositiveIntegerField(blank=True, null=True)

class DailyInventoryBySKU(models.Model):
    date = models.DateField(blank=True, null=True)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    store_house = models.ForeignKey(Store_house, on_delete=models.CASCADE)
    counts = models.PositiveIntegerField(blank=True, null=True)