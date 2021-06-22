from django.db import models
from extra_table.models import Stores

# Create your models here.
class Inventory(models.Model):
    date = models.DateField(blank=True, null=True)
    invertory = models.PositiveIntegerField(blank=True, null=True)
    stores = models.ForeignKey(Stores, on_delete=models.CASCADE)
