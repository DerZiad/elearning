from Grammar.models import Ubung,Essai

ubungs = Ubung.objects.all()
dic = {}
for ubung in ubungs:

    dic[ubung.frage] = Essai.objects.get(numf=ubung)
list = []
i = 1
for ubung in ubungs:
    list.append("ubung" + i + "= Ubung(frage=" + ubung.frage + ",losung=" + ubung.losung)
    list.apped("ubung" + i + ".save()")
    i += 1
listp = []
for ubung in ubungs:
    essai = dic[ubung.frage]
    i = 1
    for ess in essai:
        listp.append("essai" + i + " =" +'Essai(choix = '+ess.choix + ",numf=ubung"+i)
        listp.append("essai"+i +".save()")
f= open("base.py","w")
for ele in list:
    f.write(ele)
for ele in listp:
    f.write(ele)
