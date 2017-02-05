from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.home, name='home'),
  url(r'^restaurantes/$', views.restaurantes, name='restaurantes'),
  url(r'^home/$', views.home, name='home'),
]
