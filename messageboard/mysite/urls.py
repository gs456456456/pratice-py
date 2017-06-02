"""ch08www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from mysite import views


app_name = 'mysite'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/(\w+)/$', views.index,name='index'),
    url(r'^list/$', views.listing,name='list'),
    url(r'^post/$', views.posting,name='post'),
    url(r'^post2db/$', views.post2db,name='post2'),
    url(r'^contact/$', views.contact,name='contact'),
]
