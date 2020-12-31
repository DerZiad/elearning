from django.urls import path
from . import views
app_name = "Authentification"
urlpatterns = [
    path("signup",views.inscription,name = "signup"),
    path("signin",views.seconnecter,name="signin"),
    path("confirm", views.seconnecter, name="confirm"),
    path("disconnect",views.disconnect,name="disconnect")
]