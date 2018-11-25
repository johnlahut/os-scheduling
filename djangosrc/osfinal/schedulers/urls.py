from django.urls import path
from . import views

app_name = 'schedulers'

urlpatterns = [
    path('', views.sched_home, name='sched_home'),
    path('api/fcfs/', views.fcfs_api, name='fcfs_api'),
    path('api/sjf/', views.sjf_api, name='sjf_api'),
    path('api/pri/', views.pri_api, name='pri_api'),
]