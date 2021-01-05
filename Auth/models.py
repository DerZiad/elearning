from django.db import models

class Professeur(models.Model):
   pass
class Personne(models.Model):
   email = models.EmailField(max_length=25)
   password = models.CharField(max_length=80)

   nom = models.CharField(max_length=20)
   prenom = models.CharField(max_length=20)
   datedenaissance = models.CharField(max_length=50,default="02-01-2002")
   username = models.CharField(max_length=18)
   telephone = models.CharField(max_length=18,default="0652518306")

   #Succes
   succes_schreiben = models.IntegerField(default=0)
   succes_lesen = models.IntegerField(default=0)
   succes_horen = models.IntegerField(default=0)
   succes_grammar = models.IntegerField(default=0)
   #Professor
   datecreationaccount = models.DateField(auto_now_add=True)


