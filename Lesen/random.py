# choose a random element from a list
from random import seed
from random import choice
from .models import Text
def generateRandom():
    sequence = [i for i in range(3)]
    # make choices from the sequence
    return choice(sequence)
def generateRandoms(sequence):
    return choice(sequence)

def getRandomText(ubungs,request):
    textes = Text.objects.all()
    listid = []
    for text in textes:
        for ubung in ubungs:
            if text == ubung.numtext:
                listid.append(text.id)
    idtext = generateRandoms(listid)
    texto = Text.objects.get(id= int(idtext))
    return texto
