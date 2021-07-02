from django.urls import path
import inventory.views as views

app_name = 'inventory'
urlpatterns=[
    path('', views.inventory_report, name='inventory'),
    path('upload_inventory', views.upload_inventory, name='upload_inventory'),
    path('inventory_report', views.inventory_report, name='inventory_report'),
    path('download/<filename>', views.download, name='download')
    ]


