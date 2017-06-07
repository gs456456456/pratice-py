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
