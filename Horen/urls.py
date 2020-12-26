from django.urls import path
from . import views

app_name = "Horen"
urlpatterns = [
    path('', views.Horen , name='Horen'),
    path('modeltest1/', views.modeltest1 , name='ModelTest1'),
    path('modeltest2/', views.modeltest2 , name='ModelTest2'),
    path('modeltest3/', views.modeltest3 , name='ModelTest3'),
    path('poadcast/', views.poadcast, name='Poadcast'),
]