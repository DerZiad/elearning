from django.db import models


class Ubung(models.Model):
    frage = models.CharField(max_length=200)
    losung = models.IntegerField()


    def __str__(self):
        return self.frage
