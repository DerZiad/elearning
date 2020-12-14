from django.db import models

# Create your models here.
class Personne(models.Model):
   nom = models.CharField(max_length=20)
   prenom = models.CharField(max_length=20)
   datedenaissance = models.CharField(max_length=50,default="02-01-2002")
   username = models.CharField(max_length=18)
   telephone = models.CharField(max_length=18,default="0652518306")
   #Professor
   email = models.EmailField(max_length=25)
   password = models.CharField(max_length=25)
   datecreationaccount = models.DateField(auto_now_add=True)

class Professeur(Personne):
   pass
