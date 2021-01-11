from django.contrib import admin
from Auth.models import Personne
from Grammar.models import Ubung, Essai, Quiz, Tipps, Choix



admin.site.register(Personne)
admin.site.register(Ubung)
admin.site.register(Essai)
admin.site.register(Quiz)
admin.site.register(Tipps)
admin.site.register(Choix)