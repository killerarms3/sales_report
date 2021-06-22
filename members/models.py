from django.db import models
from extra_table.models import Stores

# Create your models here.
class Members(models.Model):
    date = models.DateField(blank=True, null=True)
    new = models.PositiveIntegerField(blank=True, null=True)
    total = models.PositiveIntegerField(blank=True, null=True)
    eff_new = models.PositiveIntegerField(blank=True, null=True)
    eff_total = models.PositiveIntegerField(blank=True, null=True)
    label = models.CharField(max_length=256, blank=True, null=True)