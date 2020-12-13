from django.db import models

# Create your models here.
class Personne(models.Model):
   nom = models.CharField(max_length=20)
   prenom = models.CharField(max_length=20)
   datedenaissance = models.DateField
   username = models.CharField(max_length=18)
   telephone = models.CharField(max_length=18)
   #Professor
   email = models.EmailField(max_length=25)
   password = models.CharField(max_length=25)
   datecreationaccount = models.DateField(auto_created=True)

class Professeur(Personne):
   pass
