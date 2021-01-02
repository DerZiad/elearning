from sys import path

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views
app_name="Grammar"
urlpatterns =[
    url(r'^frage', views.grammarex,name="frage"),
    url(r'^$', views.cours,name="grammar"),
    url(r'^gegenteile',views.gegenteile,name="gegenteile"),
    url(r'^bestimmte-artikel',views.bartikel,name="bestimmte artikel"),
    url(r'^register',views.test,name="register")
]