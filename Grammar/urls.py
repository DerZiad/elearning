from sys import path

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = "Grammar"
urlpatterns = [
    url(r'^frage', views.grammarex, name="frage"),
    url(r'^ubung', views.ubung, name="grammar"),
    url(r'^gegenteile', views.gegenteile, name="gegenteile"),
    url(r'^bestimmte-artikel', views.bartikel, name="bestimmte artikel"),
    url(r'^register', views.test, name="register"),

    url(r'^alphabet', views.alphabet, name="alphabet"),
    url(r'^menuCours', views.menu, name="menuCours"),
    url(r'^artikel', views.artikel, name="artikel"),
    url(r'^pronomscours', views.pronoms, name="pronoms"),
    url(r'^adjektive', views.adjektive, name="adjektive"),
    url(r'^pronomsindefinis', views.pronomsindefinis, name="pronomsindefinis"),
    url(r'^pronompersonnels', views.pronompersonnels, name="pronompersonnels"),
    url(r'^adverbes', views.adverbs, name="adverbes"),
    url(r'^numeraux',views.numeraux,name="numeraux"),
    url(r'^unbestimmte-artikel',views.ua,name="unbes-art"),
    url(r'^$', views.general, name="menu")
]
