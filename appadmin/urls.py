#-*- coding:utf-8 -*-
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.views import static
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<id>[0-9]+)/vote/$', views.vote, name='vote'),
]
