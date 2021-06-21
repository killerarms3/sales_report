from django.db import models
from extra_table.models import Stores

# Create your models here.
class smt_report(models.Model):
    date = models.DateField(blank=True, null=True)
    sales = models.PositiveIntegerField(blank=True, null=True)
    sales_budget = models.PositiveIntegerField(blank=True, null=True)
    margin = models.PositiveIntegerField(blank=True, null=True)
    margin_budget = models.PositiveIntegerField(blank=True, null=True)
    stores = models.ForeignKey(Stores, on_delete=models.CASCADE)