from django.contrib import admin
from Horen.models import ModelTest,Track
from Auth.models import Personne, Professeur
from Grammar.models import Ubung, Essai

admin.site.register(ModelTest)
admin.site.register(Track)
admin.site.register(Personne)
admin.site.register(Professeur)
admin.site.register(Ubung)
admin.site.register(Essai)
