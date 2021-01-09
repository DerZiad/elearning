from django.urls import path
from . import views
app_name = "Authentification"
urlpatterns = [
    path("signup",views.inscription,name = "signup"),
    path("signin",views.seconnecter,name="signin"),
    path("confirm", views.confirm, name="confirm"),
    path("disconnect",views.disconnect,name="disconnect"),
    path("recover",views.recoverPassword,name="recover"),
    path("delete",views.suprimerNotValid,name="delete")
]