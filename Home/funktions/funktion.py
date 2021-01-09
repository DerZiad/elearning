from Auth.models import Personne


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
