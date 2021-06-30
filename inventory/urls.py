from django.urls import path
import inventory.views as views

app_name = 'inventory'
urlpatterns=[
    path('upload_inventory', views.upload_inventory, name='upload_inventory'),
    ]


