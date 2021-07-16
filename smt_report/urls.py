from django.urls import path
import smt_report.views as views

app_name = 'smt_report'
urlpatterns=[
    path('', views.members_report, name='smt_report'),
    path('smt_report', views.members_report, name='smt_report_report'),
    path('download/<filename>', views.download, name='download')
    ]