from django.db import models


from Auth.models import Personne


class Text (models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
class Ubung(models.Model):
    frage = models.CharField(max_length=200)
    losung = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    numtext = models.ForeignKey(Text, on_delete=models.CASCADE)
    def __str__(self):
        return self.frage
class Reponse(models.Model):
    ubung = models.OneToOneField(Ubung, on_delete=models.CASCADE)
    pers= models.ForeignKey(Personne, on_delete=models.CASCADE,related_name='perso')
    valide = models.BooleanField(default=False)

class Essai(models.Model):
    choix = models.CharField(max_length=15)
    numf = models.ForeignKey(Ubung, on_delete=models.CASCADE)


# Create your models here.
