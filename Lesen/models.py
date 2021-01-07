from django.db import models


class Text (models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()


class Fragen (models.Model):
    id = models.IntegerField(primary_key=True)
    frage = models.TextField()
    losung = models.SmallIntegerField()
    numtext = models.ForeignKey(Text, on_delete=models.CASCADE)


class Answers (models.Model):
    an = models.CharField(max_length=20)
    numfra = models.ForeignKey(Fragen, on_delete=models.CASCADE)


# Create your models here.
