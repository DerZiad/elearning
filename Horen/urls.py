from django.urls import path
from . import views

app_name = "Horen"
urlpatterns = [
    path('', views.index , name='index'),
    path('poadcast/', views.poadcast, name='Poadcast'),
]