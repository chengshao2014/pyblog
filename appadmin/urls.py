#-*- coding:utf-8 -*-
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.views import static
from django.views.generic import RedirectView
from .views import MyView
urlpatterns = [
    url(r'^login$', MyView.as_view(), name='my-view'),
    url(r'^login&r=login.html$', views.login, name='login'),
    url(r'^$', RedirectView.as_view(url='http://py68.com:10000/appadmin/login&r=login.html'), name='django')
    # url(r'^$', views.index, name='index'),
    # url(r'^index$', views.index),
    # url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<id>[0-9]+)/vote/$', views.vote, name='vote'),
]
