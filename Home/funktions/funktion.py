from Auth.models import Personne

def getSuccess(nomsuccess,request):
    username = request.session["username"]
    personne = Personne.objects.get(username=username)
    if nomsuccess == "succes_lesen":
        return personne.succes_lesen
    elif nomsuccess == "succes_horen":
        return personne.succes_horen
    elif nomsuccess == "succes_grammar":
        return personne.succes_grammar
    else:
        raise IndexError

def saveSucess(nomsuccess,valeur,request):
    username = request.session["username"]
    personne = Personne.objects.get(username=username)
    if nomsuccess == "succes_lesen":
        personne.succes_lesen = int(valeur)
        personne.save()
    elif nomsuccess == "succes_horen":
        personne.succes_horen = int(valeur)
        personne.save()
    elif nomsuccess == "succes_grammar":
        personne.succes_grammar = int(valeur)
        personne.save()
    else:
        raise IndexError


def getName(photo):
    name = photo.name
    ele = name[0:int(name.index('.'))]
    extension = name[name.index('.'):len(name)]
    test = extension.lower()
    if test != ".jpeg" and test != ".jpg" and test != ".png":
        raise ValueError
    photo.name = str(hash(ele)) + extension
    return photo


def checkSession(request):
    try:
        username = request.session['username']
        personne = Personne.objects.get(username=username)
        if not personne.valid:
            raise IndexError
    except:
        raise IndexError
