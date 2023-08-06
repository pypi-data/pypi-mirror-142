from django.urls import path

from ad_import import views

app_name = 'ad_import'

urlpatterns = [
    path('user', views.view_user, name='user'),
    path('computer', views.view_workstation, name='workstation'),
    path('server', views.view_server, name='server'),
]
