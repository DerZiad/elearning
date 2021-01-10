from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Home.funktions.funktion import checkSession
from Lesen.models import Text, Fragen, Answers


def listing(request):
    # try:
    # checkSession(request)
    if request.method == "GET":
        texts = Text.objects.all()
        fragen = Fragen.objects.all()
        answers = Answers.objects.all()
        dic1 = {
        }
        dic = {
        }
        liste = []
        for texte in texts:
            dic1[str(texte.title)] = texte.text
            for frag in fragen:
                if frag.numtext == texte:
                    for ans in answers:
                        if ans.numfra == frag:
                            liste.append(ans.an)

                dic[str(frag.frage)] = liste
                liste = []

        context = {
            'dictionnaire_text': dic1,
            'dictionnaire_ans': dic
        }
        return render(request, 'Lesen/ubungs.html', context)
    else:
        fragen = Fragen.objects.all()
        answers = Answers.objects.all()
        losung = request.POST
        validator = {}
        reponsejuste = {}
        erreurfausse = {}
        cmp = 0
        try:
            if str(losung[fragen.frage]) == fragen.losung:
                cmp += 1
                validator[fragen.frage] = True
                reponsejuste[fragen.frage] = losung[fragen.frage]
            else:
                validator[fragen.frage] = False
                erreurfausse[fragen.frage] = losung[fragen.frage]
                reponsejuste[fragen.frage] = fragen.losung
        except:
            msg = "Veuillez répondre a toutes les questions les questions "
# except:
# return HttpResponseRedirect("/")

# Create your views here.
