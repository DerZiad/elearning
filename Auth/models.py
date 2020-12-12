from django.db import models

# Create your models here.
class Personne(models.Model):
   nom = models.CharField(max_length=20)
   prenom = models.CharField(max_length=20)
   datedenaisse = models.DateField
   username = models.CharField(max_length=20)
   #Professor
   email = models.EmailField(max_length=40)
   password = models.CharField(max_length=50)
   datecreationaccount = models.DateField(auto_created=True)

class Professor(Person):
   pass
