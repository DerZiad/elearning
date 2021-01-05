app_name = "Schreiben"
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="homeschreiben"),
    path("correction",views.correction,name="correction")
]