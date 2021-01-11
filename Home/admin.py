from django.contrib import admin
from Auth.models import Personne
from Grammar.models import Ubung, Essai
from Lesen.models import Text, Fragen, Answers
from Horen.models import *
admin.site.register(Answers)
admin.site.register(Text)
admin.site.register(Fragen)
admin.site.register(Personne)
admin.site.register(Ubung)
admin.site.register(Essai)
admin.site.register(ModelTest)
admin.site.register(Track)
admin.site.register(Question)
admin.site.register(Choix)
