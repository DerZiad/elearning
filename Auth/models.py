from django.db import models

class Professeur(models.Model):
   pass
class User(models.Model):
   email = models.EmailField(max_length=25)
   password = models.CharField(max_length=25)
   nom = models.CharField(max_length=20)
   prenom = models.CharField(max_length=20)
   datedenaissance = models.CharField(max_length=50,default="02-01-2002")
   username = models.CharField(max_length=18)
   telephone = models.CharField(max_length=18,default="0652518306")
   #Professor
   datecreationaccount = models.DateField(auto_now_add=True)

class Succes(models.Model):
   succes_schreiben = models.IntegerField()
   succes_lesen = models.IntegerField()
   succes_horen = models.IntegerField()
   succes_grammar = models.IntegerField()
   users = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
