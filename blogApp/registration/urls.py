__author__ = 'abhishekrathore'

from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^create/', views.create, name='create'),
    url(r'^register/', views.register, name='register'),
    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),


]
