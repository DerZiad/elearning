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
    username = request.session['username']
    if username == None and len(username) == 0:
        raise IndexError