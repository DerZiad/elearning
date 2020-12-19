from django.db import models

# Create your models here.
class Personne:
   nom = models.CharField(max_length=20)
   prenom = models.CharField(max_length=20)
   datedenaissance = models.CharField(max_length=50,default="02-01-2002")
   username = models.CharField(max_length=18)
   telephone = models.CharField(max_length=18,default="0652518306")
   #Professor
   datecreationaccount = models.DateField(auto_now_add=True)

class Professeur(Personne,models.Model):
   pass
class User(Personne,models.Model):
   email = models.EmailField(max_length=25)
   passord = models.CharField(max_length=25)
class Succes(models.Model):
   succes_schreiben = models.IntegerField()
   succes_lesen = models.IntegerField()
   succes_horen = models.IntegerField()
   succes_grammar = models.IntegerField()
   users = models.ManyToManyField(User,related_name="succes",blank=True)
