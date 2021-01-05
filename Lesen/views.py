from django.shortcuts import render

from Lesen.models import Text, Fragen, Answers


def listing(request):
    if request.method == "GET":
        texts = Text.objects.all()
        fragen = Fragen.objects.all()
        answers = Answers.objects.all()

        dic = {
        }
        list = []
        for texte in texts:
            list.append(texte.text)
            for frag in fragen:

                if frag.numtext == texte:
                    list.append(frag.frage)
                    for ans in answers:
                        if ans.numfra == frag:
                            list.append(ans.an)
                list = []
                dic[str(texte.title)] = list

    context = {
        'dictionnaire': dic
    }
    return render(request, 'Lesen/ubungs.html', context)

# Create your views here.
