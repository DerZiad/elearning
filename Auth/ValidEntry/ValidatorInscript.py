from Auth.models import Personne

def checkFirstPanelInBase(request):
    dictionnaire = request.POST
    email = dictionnaire['email']
    emails = Personne.objects.filter(email=email)
    erreurs = {}
    if(len(emails) != 0):
        erreurs['email'] = "L'adresse email est déja existante"
    return erreurs

def checkSecondPaneInBase(request):
    dictionnaire = request.POST
    username = dictionnaire['username']

    usernames = Personne.objects.filter(username = username)
    erreurs = {}
    if(len(usernames) != 0):
        erreurs['username'] = "Le pseudo user que vous avez entrée est dèja existant"
    return erreurs
