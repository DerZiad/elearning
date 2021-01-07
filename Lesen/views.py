from django.shortcuts import render

from Lesen.models import Text, Fragen, Answers


def listing(request):
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

# Create your views here.
