from django.urls import path
from . import views
urlpatterns = [
    path("signup",views.inscription,name = "signup"),
    path("signin",views.seconnecter,name="signin")

]