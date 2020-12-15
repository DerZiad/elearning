from Auth.models import Personne

def checkFirstPanelInBase(request):
    dictionnaire = request.POST
    email = dictionnaire['email']
    telephone = dictionnaire['telephone']


    emails = Personne.objects.filter(email=email)
    telephones = Personne.objects.filter(telephone=telephone)

    erreurs = {}
    if(emails.len() != 0):
        erreurs['email'] = "L'adresse email est déja existante"
    if(telephones.len() != 0):
        erreurs['telephone'] = "Le numero de téléphone est déja existant"
    return erreurs

def checkSecondPaneInBase(request):
    dictionnaire = request.POST
    username = dictionnaire['username']

    usernames = Personne.objects.filter(username = username)
    erreurs = {}
    if(usernames.len() != 0):
        erreurs['username'] = "Le pseude user que vous avez entrée est dèja existant"
