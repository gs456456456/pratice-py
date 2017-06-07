# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from dairy import views


app_name = 'dairy'

urlpatterns = [
    url(r'^login/$', views.login,name='login'),
    url(r'^loginafter/', views.login_after,name='login_after'),
    url(r'^loginout/',views.logout,name = 'login_out'),
    url(r'^register/',views.register,name='register'),
    url(r'^daily/',views.daily,name='daily'),
    url(r'^list/',views.list2,name='list')
]
