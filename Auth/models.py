from django.db import models
class Personne(models.Model):
   email = models.EmailField(max_length=25)
   password = models.CharField(max_length=80)

   nom = models.CharField(max_length=20)
   prenom = models.CharField(max_length=20)
   datedenaissance = models.DateField()
   username = models.CharField(max_length=18)
   Address = models.CharField(max_length=80)
   Sexe = models.CharField(max_length=5)
   photo = models.ImageField(upload_to="pictures/", max_length=255, default="pictures/user_200_200.jpg")

   #Succes
   succes_schreiben = models.IntegerField(default=0)
   succes_lesen = models.IntegerField(default=0)
   succes_horen = models.IntegerField(default=0)
   succes_grammar = models.IntegerField(default=0)
   #Professor
   datecreationaccount = models.DateField(auto_now_add=True)

class temporals(models.Model):
      code = models.CharField(max_length=10, primary_key=True)
      personne = models.ForeignKey(Personne, on_delete=models.CASCADE)


