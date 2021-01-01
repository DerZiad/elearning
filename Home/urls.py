from django.urls import path
app_name = "Home"
from . import views
urlpatterns = [
    path("",views.principale,name = "signup"),
    path("afficher",views.afficherProfil,name = "afficher"),
    path("impressum",views.impressum,name = "impressum"),
    path("essatials/allemagne",views.informationsgerman,name="germaninfo"),
    path("essatials/autriche",views.informationsgerman,name="autricheinfo"),
    path("essatials/",views.infos,name="info")

]