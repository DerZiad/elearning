from django.contrib import admin
from Auth.models import Personne
from Grammar.models import *
import Horen.models as yasser
admin.site.register(Personne)
admin.site.register(Ubung)
admin.site.register(Essai)
admin.site.register(yasser.Choix)
admin.site.register(yasser.ModelTest)
admin.site.register(yasser.Track)
admin.site.register(yasser.Question)
admin.site.register(yasser.ReponseHoren)