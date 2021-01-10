from django.conf.urls import url
from Lesen import views

app_name = "Lesen"
urlpatterns = [
    url(r'^$', views.generateText,name="exo"),
]