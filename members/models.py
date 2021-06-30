from django.db import models
from extra_table.models import Stores, CRM_tags 

# Create your models here.
class Members(models.Model):
    date = models.DateField()
    new = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    eff_new = models.PositiveIntegerField()
    eff_total = models.PositiveIntegerField()
    label = models.ForeignKey(CRM_tags, on_delete=models.CASCADE)
