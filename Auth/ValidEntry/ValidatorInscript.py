from Auth.models import User

def checkFirstPanelInBase(request):
    dictionnaire = request.POST
    email = dictionnaire['email']
    telephone = dictionnaire['telephone']


    emails = User.objects.filter(email=email)
    telephones = User.objects.filter(telephone=telephone)

    erreurs = {}
    if(len(emails) != 0):
        erreurs['email'] = "L'adresse email est déja existante"
    if(len(telephones) != 0):
        erreurs['telephone'] = "Le numero de téléphone est déja existant"
    return erreurs

def checkSecondPaneInBase(request):
    dictionnaire = request.POST
    username = dictionnaire['username']

    usernames = User.objects.filter(username = username)
    erreurs = {}
    if(len(usernames) != 0):
        erreurs['username'] = "Le pseudo user que vous avez entrée est dèja existant"
    return erreurs
