from Schreiben.models import Reponse,Excercice
from Auth.models import Personne
from random import seed
from random import choice
def generateRandom(sequence):
    return choice(sequence)
def getSchreiben(request):
    exercices = Excercice.objects.all()
    personne = Personne.objects.get(username=request.session['username'])
    reponses = Reponse.objects.filter(personne = personne)
    listexercices = []
    for exo in exercices:
        rep = Reponse.objects.filter(excercice = exo)
        if len(rep) == 0:
            listexercices.append(exo)
    return generateRandom(listexercices)