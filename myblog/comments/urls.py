from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^post/(?P<post_pk>[0-9]+)/$',views.comments,name = 'comments')

]