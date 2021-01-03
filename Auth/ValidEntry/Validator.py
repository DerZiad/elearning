from django import forms
import re
from Auth.models import Personne
# Make a regular expression
# for validating an Email
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


# for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

# Define a function for
# for validating an Email
def validinfo(username,email):
    personne1 = Personne.objects.filter(email = email)
    personne2 = Personne.objects.filter(username = username)
    if len(personne1) != 0 or len(personne2) != 0:
        raise ValueError
def validEmail(email):
    # pass the regular expression
    # and the string in search() method
    if (not re.search(regex, email)):
        raise ValueError

def validNom(nom):
    if len(nom) <2 or len(nom) >20:
        raise ValueError
def validPrenom(prenom):
    if len(prenom) < 2 or len(prenom) > 20:
        raise ValueError
def validSexe(sexe):
    if sexe != "Homme" and sexe != "Femme":
        raise ValueError
def validDate(list):
    try:
        for ele in list:
            int(ele)
    except TypeError:
        raise ValueError
def validAdress(adress):
    if len(adress) < 10 or len(adress) > 40:
        raise ValueError