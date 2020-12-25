def converttodata(request,user):
    attributs = request.session
    attributs["nom"] = user.nom
    attributs["prenom"] = user.prenom,
    attributs["datedenaissance"] = user.datedenaissance
    attributs["username"] = user.username
    attributs["telephone"] = user.telephone,
    attributs["email"] =  user.email
    attributs["password"] =  user.password
    attributs["succes_lesen"] = user.succes_lesen
    attributs["succes_horen"] = user.succes_horen
    attributs["succes_schreiben"] = user.succes_schreiben
    attributs["succes_grammar"] = user.succes_grammar


def testerSession(request):
    user = request.session.get('username')
    if(user == None or len(user) == 0):
        return False
    else:
        return True
