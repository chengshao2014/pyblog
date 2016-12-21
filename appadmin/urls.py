#-*- coding:utf-8 -*-
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.views import static
from django.views.generic import RedirectView
from .views import MyView
urlpatterns = [
    # url(r'^login$', MyView.as_view(), name='my-view'),
    url(r'^login$', views.admin_login),
    url(r'^form$', views.blog_form),
    url(r'^index$',views.blog_index),
    url(r'^$', views.blog_form, name='index'),
    url(r'^(?P<id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^code', views.code),
    # url(r'^index$', views.index),
    # url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^login&r=login.html$', MyView.as_view('login'), name='login'),
    # url(r'^$', RedirectView.as_view(url='http://py68.com:10000/appadmin/login&r=login.html'), name='django'),
]
