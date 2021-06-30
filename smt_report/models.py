from django.db import models
from extra_table.models import Stores

# Create your models here.
class smt_report(models.Model):
    date = models.DateField()
    sales = models.IntegerField()
    sales_budget = models.PositiveIntegerField()
    margin = models.IntegerField()
    margin_budget = models.PositiveIntegerField()
    stores = models.ForeignKey(Stores, on_delete=models.CASCADE)
