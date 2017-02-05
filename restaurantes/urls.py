from django.conf.urls import url

from . import views
from flask_pymongo import PyMongo
import pymongo

urlpatterns = [
  url(r'^$', views.home, name='home'),
  url(r'^restaurantes/$', views.restaurantes, name='restaurantes'),
  url(r'^home/$', views.home, name='home'),
  url(r'^getrestaurantes/$', views.getDatosRestaurantes, name='getDatosRestaurantes'),
  url(r'^addrestaurantes$', views.addrestaurantes, name='addrestaurantes'),
]
