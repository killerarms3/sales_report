from django.db import models
from extra_table.models import Store_house

# Create your models here.
class Inventory(models.Model):
    date = models.DateField(blank=True, null=True)
    inventory = models.IntegerField(blank=True, null=True)
    store_house = models.ForeignKey(Store_house, on_delete=models.CASCADE)
