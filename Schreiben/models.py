from django.db import models


# Create your models here.
class text(models.Model):
    titre = models.CharField(max_length=200, unique=True)
    corps = models.CharField(max_length=300)


class Reponse(models.Model):
    rep = models.TextField(blank=True, null=True)
    #txt = models.ForeignKey(text, on_delete=models.CASCADE)


