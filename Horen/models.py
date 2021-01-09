from django.db import models
from Auth.models import Personne

class ModelTest(models.Model):
    titre = models.CharField(max_length=30)
    niveau= models.CharField(max_length=3, default='A1')
    note= models.IntegerField(default=0)
    def __str__(self):
        return self.titre+' niveau '+self.niveau

class Track(models.Model):
    trackname= models.CharField(max_length=30, default=None)
    track= models.FileField(upload_to='Track/')
    modeltest = models.ForeignKey(ModelTest,default=None , on_delete=models.CASCADE)
    def __str__(self):
        return self.trackname +'-'+ self.modeltest.titre

class Question(models.Model):
    quest = models.CharField(max_length=150)
    reponse= models.CharField(max_length=150)
    audio = models.OneToOneField(Track,on_delete=models.CASCADE)
    def __str__(self):
        return self.quest+'-'+self.audio.trackname

class Choix(models.Model):
    choix= models.CharField(max_length=150)
    question= models.ForeignKey(Question,default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.choix
