def converttodata(request,user):
    attributs = request.session
    attributs["nom"] = user.nom
    attributs["prenom"] = user.prenom,
    attributs["datedenaissance"] = user.datedenaissance
    attributs["username"] = user.username
    attributs["telephone"] = user.telephone,
    attributs["email"] =  user.email
    attributs["password"] =  user.password


