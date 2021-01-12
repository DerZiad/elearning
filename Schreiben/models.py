from django.db import models
from Auth.models import Personne


class Excercice(models.Model):
    text = models.TextField(blank=True)
    sujet = models.CharField(max_length=50)


class Reponse(models.Model):
    rep = models.TextField(blank=True, null=True)
    legal = models.BooleanField(default=False)
    corrected = models.BooleanField(default=False)
    excercice = models.ForeignKey(Excercice, on_delete=models.CASCADE)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
class Correction(models.Model):
    text = models.TextField()
    remarque = models.TextField()
    reponse = models.OneToOneField(Reponse,on_delete=models.CASCADE,null=True)