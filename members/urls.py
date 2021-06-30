from django.urls import path
import members.views as views

app_name = 'members'
urlpatterns=[
    path('members_report', views.members_report, name='members_report'),
    path('download/<filename>', views.download, name='download')
    ]


