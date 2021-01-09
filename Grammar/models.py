from django.db import models


class Ubung(models.Model):
    frage = models.CharField(max_length=200)
    losung = models.CharField(max_length=200)

    def __str__(self):
        return self.frage


class Essai(models.Model):
    choix = models.CharField(max_length=15)
    numf = models.ForeignKey(Ubung, on_delete=models.CASCADE)


class Quiz(models.Model):
    jeu = models.TextField(max_length=500)
    losung = models.TextField(max_length=200)


class Tipps(models.Model):
    titre = models.CharField(max_length=20)
    text = models.TextField(max_length=100)
    NQ = models.OneToOneField(Quiz, on_delete=models.CASCADE)


class Choix(models.Model):
    mog = models.CharField(max_length=15)
    numf = models.ForeignKey(Quiz, on_delete=models.CASCADE)
