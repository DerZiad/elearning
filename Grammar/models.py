from django.db import models







class Ubung(models.Model):
    frage = models.CharField(max_length=200)
    losung = models.CharField(max_length=200)
    moglich = models.TextField()
    def __str__(self):
        return self.frage
class Essai(models.Model):
    test =models.CharField(max_length=15)
    ayman=models.ForeignKey(Ubung,on_delete=models.CASCADE)

