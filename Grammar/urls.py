from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views
app_name="Grammar"
urlpatterns =[
    url(r'^$', views.grammarex),

]