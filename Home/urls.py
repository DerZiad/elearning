from django.urls import path
app_name = "Home"
from . import views
urlpatterns = [
    path("",views.principale,name = "signup"),
]