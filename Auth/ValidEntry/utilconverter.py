def converttodata(request,user):
    attributs = request.session
    attributs["nom"] = user.nom
    attributs["prenom"] = str(user.prenom)
    birthday = user.datedenaissance
    attributs["datedenaissance"] = str(birthday.day) + '-' +  str(birthday.month) + '-' + str(birthday.year)
    attributs["username"] = user.username
    attributs["sexe"] = str(user.Sexe)
    attributs['address'] = str(user.Address)
    attributs["email"] =  str(user.email)
    attributs["password"] =  user.password
    attributs["succes_lesen"] = user.succes_lesen
    attributs["succes_horen"] = user.succes_horen
    attributs["succes_grammar"] = user.succes_grammar


def testerSession(request):
    user = request.session.get('username')
    if(user == None or len(user) == 0):
        return False
    else:
        return True
