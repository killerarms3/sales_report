from django.contrib import admin
from extra_table.models import Stores, SKU, Store_house, CRM_tags
# Register your models here.

@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'category',
        'subtype'
    )

@admin.register(SKU)
class SKUAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'cost',
        'status'
    )

@admin.register(Store_house)
class StoreHouseAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'category',
        'subtype'
    )

@admin.register(CRM_tags)
class CRMTagAdmin(admin.ModelAdmin):
    list_display = (
        'tag',
        'category',
        'subtype'
    )
