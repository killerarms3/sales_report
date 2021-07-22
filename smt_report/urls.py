from django.urls import path
import smt_report.views as views

app_name = 'smt_report'
urlpatterns=[
    path('', views.smt_report, name='smt_report'),
    path('upload_smt', views.upload_smt, name='upload_smt'),
    #path('smt_report', views.smt_report_report, name='smt_report_report'),
    #path('download/<filename>', views.download, name='download')
    ]