from django.db import models

from Auth.models import Personne


class Ubung(models.Model):
    frage = models.CharField(max_length=200)
    losung = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    def __str__(self):
        return self.frage
class Reponse(models.Model):
    ubung = models.OneToOneField(Ubung, on_delete=models.CASCADE)
    pers= models.ForeignKey(Personne, on_delete=models.CASCADE,related_name='pers')
    valide = models.BooleanField(default=False)

class Essai(models.Model):
    choix = models.CharField(max_length=15)
    numf = models.ForeignKey(Ubung, on_delete=models.CASCADE)
