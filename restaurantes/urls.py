from django.conf.urls import url

from . import views
from flask_pymongo import PyMongo
import pymongo

urlpatterns = [
  url(r'^$', views.home, name='home'),
  url(r'^restaurantes/$', views.restaurantes, name='restaurantes'),
  url(r'^home/$', views.home, name='home'),
  url(r'^getrestaurantes/$', views.getrestaurantes, name='getrestaurantes'),
  url(r'^addrestaurantes$', views.addrestaurantes, name='addrestaurantes'),
  url(r'^getinfo/$', views.getinfo, name='getinfo'),
  url(r'^getallrestaurantes/$', views.getallrestaurantes, name='getallrestaurantes'),
  url(r'^gettweets/$', views.gettweets, name='gettweets'),
]
