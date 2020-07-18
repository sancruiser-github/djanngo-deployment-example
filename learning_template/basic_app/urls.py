from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpattern = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other')
]