from django.contrib import admin
from Auth.models import Personne, Professeur
from Grammar.models import Ubung, Essai


admin.site.register(Personne)
admin.site.register(Professeur)
admin.site.register(Ubung)
admin.site.register(Essai)
