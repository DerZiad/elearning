from django.shortcuts import render
from django.template import loader
from .models import Message
from Auth.models import  Personne
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from Home.funktions.funktion import getName
import hashlib
import Auth.ValidEntry.sender as sender
import Auth.ValidEntry.random as randomer
import Auth.ValidEntry.Validator as valid
import datetime
# Create your views here.

def principale(request):
    StringUser = request.session.get('username')
    if(StringUser == None or len(StringUser) == 0):
        template = loader.get_template("Home.html")
        return HttpResponse(template.render(request=request))
    else:
        succes_grammar = request.session['succes_lesen']
        succes_schreiben = request.session['succes_schreiben']
        succes_horen = request.session['succes_horen']
        succes_lesen = request.session['succes_lesen']
        total = int((succes_lesen + succes_horen + succes_schreiben + succes_grammar) / 4)
        context = {
            'total': total
        }
        return render(request, "session/session.html", context)

def afficherProfil(request):
    user = request.session['username']
    if(user == None or len(user) <= 0):
        return HttpResponseRedirect("/")
    else:
        context = {
            "personne":Personne.objects.get(username = request.session['username'])
        }
        return render(request,"afficher/profil.html",context)

def impressum(request):
    template = loader.get_template("impressum.html")
    return HttpResponse(template.render())
def informationsgerman(request):
    template = loader.get_template("Info/German.html")
    return HttpResponse(template.render())
def informationsautriche(request):
    template = loader.get_template("Info/Autriche.html")
    return HttpResponse(template.render())
def infos(request):
    try:
        id = request.POST['id']
        if(id == '1'):
            informationsgerman(request)
        elif(id == '2'):
            informationsautriche(request)
        else:
            return render(request,"Info/info.html")
    except:
        return render(request, "Info/info.html")
def forum(request):
    if(request.method=='GET'):
        messages = Message.objects.all()
        paginator = Paginator(messages,5)
        idpage = request.GET.get('page')
        try:
            messagesG = paginator.page(idpage)
        except PageNotAnInteger:
            messagesG = paginator.page(1)
        except EmptyPage:
            messagesG = paginator.page(paginator.num_pages)
        context = {
            "messages":messagesG
        }
        return render(request,"forum/forum.html",context)
    else:
        attributs = request.POST
        sujet = attributs['subject']
        message = attributs['message']
        username = request.session['username']
        personne = Personne.objects.get(username =  username)
        messagess = Message(message = message,personne = personne,subject = sujet)
        messagess.save()
        messages = Message.objects.all()
        paginator = Paginator(messages,5)
        idpage = request.GET.get('page')
        try:
            messagesG = paginator.page(idpage)
        except PageNotAnInteger:
            messagesG = paginator.page(1)
        except EmptyPage:
            messagesG = paginator.page(paginator.num_pages)
        context = {
            "messages":messagesG
        }
        return render(request,"forum/forum.html",context)
def edit(request):
    if request.method == "POST":
        action = request.POST.get('action')
        if action == 'delete':
            personne = Personne.objects.get(username = request.session['username'])
            message = Message.objects.get(personne = personne)
            personne.delete()
            message.delete()
            request.session.flush()
            request.session.clear_expired()
            return HttpResponseRedirect("/")
        elif action == 'changeemailfirst':
            email = request.POST['email']
            passw = request.POST['password']
            cpassword = hashlib.md5(passw.encode())
            personne = Personne.objects.get(username=request.session['username'])
            context = {

            }
            if personne.password == cpassword.hexdigest():
                personnes = Personne.objects.filter(email=email)
                if len(personnes) == 0:
                    code = randomer.generateRandom()
                    request.session['code'] = code
                    request.session['nemail'] = email
                    info = {
                        "address":email,
                        "text":"Votre de code changement est " + code,
                        "subject": "Changer le code"
                    }
                    sender.sendEmail(info,request)
                    context['success'] = "Vrai"
                else:
                    context['success'] = "Faux"
                    context["errorfirst"] = "Email dèja existant"
            else:
                context['success'] = "Faux"
                context["errorfirst"] = "Mot de passe incorrect",
            return JsonResponse(context)
        elif action == 'changemailsecond':
            personne = Personne.objects.get(username = request.session['username'])
            code = request.session['code']
            codeR = request.POST.get('code')
            context = {
            }
            if code == codeR:
                personne = Personne.objects.get(email = request.session['email'])
                personne.email = request.session['nemail']
                personne.save()
                context['success'] = "Vrai"
            else:
                context['errorfirst'] = "Le code est incorrect"
            return JsonResponse(context)
        elif action == "changepassword":
            personne = Personne.objects.get(username = request.session['username'])
            normalpassword = request.POST['normalpassword']
            newpassword = request.POST['newpassword']
            cnewpassword = request.POST['cnewpassword']
            context = {

            }
            if len(newpassword) >= 9:
                if newpassword == cnewpassword:
                    encryptednewpassword = hashlib.md5(newpassword.encode()).hexdigest()
                    if hashlib.md5(normalpassword.encode()).hexdigest() == personne.password:
                        personne.password = encryptednewpassword
                        personne.save()
                        context['success'] = "Vrai"
                    else:
                        context['success'] = "Faux"
                        context["errorsecond"] = "Votre mot de passe est incorrect"

                else:
                    context['success'] = "Faux"
                    context["errorsecond"] = "Le nouveau mot de passe doit être identique au confirmation"
            else:
                context['success'] = "Faux"
                context["errorsecond"] = "le mot de passe doit être au moins 9 caractères"
            return JsonResponse(context)
        elif action == "changeinfo":
                try:
                    nom = request.POST['nom']
                    prenom = request.POST['prenom']
                    address = request.POST['address']
                    dateday = request.POST['dateday']
                    datemonth = request.POST['datemonth']
                    dateyear = request.POST['dateyear']
                    sexe = request.POST['sexe']
                    list= []
                    list.append(dateday)
                    list.append(datemonth)
                    list.append(dateyear)
                    valid.validNom(nom)
                    valid.validPrenom(prenom)
                    valid.validDate(dateday)
                    valid.validDate(list)
                    valid.validSexe(sexe)
                    personne = Personne.objects.get(username = request.session['username'])
                    personne.nom = nom
                    personne.prenom = prenom
                    personne.Address = address
                    personne.datedenaissance = datetime.date(year=int(dateyear), month=int(datemonth), day=int(dateday))
                    personne.Sexe = sexe
                    personne.save()
                    context = {
                        "personne":personne,
                    }
                    return render(request, "editor/editor.html", context)
                except ValueError:
                    personne = Personne.objects.get(username = request.session['username'])
                    context = {
                        "errorthid":"Vous avez une erreur dans votre informations",
                        "personne":personne
                    }
                    return render(request,"editor/editor.html",context)
        elif action == "changepic":
            fonction = request.POST['fonction']
            personne = Personne.objects.get(username=request.session['username'])
            if fonction == "add":
                try:
                    photo = request.FILES['photo']
                    photo = getName(photo)
                    personne.photo = photo
                    personne.save()
                except ValueError:
                    personne = Personne.objects.get(username=request.session['username'])
                    context = {
                        "personne": personne,
                        "errorimage":"Le fichier que vous voulez insérer doit être jpg ou jpeg ou png"
                    }
                    return render(request, "editor/editor.html", context)
            elif fonction == "remove":
                personne.photo = "/media"
                personne.save()
            else:
                pass
            personne = Personne.objects.get(username=request.session['username'])
            context = {
                "personne": personne
            }
            return render(request, "editor/editor.html", context)
        else:
            personne = Personne.objects.get(username=request.session['username'])
            context = {
                "personne": personne
            }
            return render(request, "editor/editor.html", context)
    else:
        personne = Personne.objects.get(username = request.session['username'])
        context = {
            "personne":personne,
        }
        return render(request,"editor/editor.html",context)

def test(request):
    return HttpResponse(loader.get_template("forum/forum.html").render())