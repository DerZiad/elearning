import os 
from Grammar.models import Essai,Ubung 
os.system("python manage.py shell") 
os.system("ubung1= Ubung(frage="'......'   ist diese Frau ?Das ist meine Mutter",losung="wer"))"
os.system("ubung1.save()")
os.system("ubung2= Ubung(frage="'........'  hast du Geburtstag ? Am 10Januar",losung="wann"))"
os.system("ubung2.save()")
os.system("ubung3= Ubung(frage="'.........'  bist du in Deutschland? Ich möchte Deutsch lernen.",losung="warum"))"
os.system("ubung3.save()")
os.system("ubung4= Ubung(frage="'........'  ist mein neues Buch? Es liegt auf dem Tisch.",losung="wo"))"
os.system("ubung4.save()")
os.system("ubung5= Ubung(frage="'......'  heisst du ? Ich heisse Sebastian",losung="was"))"
os.system("ubung5.save()")
os.system("ubung6= Ubung(frage="'....... '  wohnst du? Ich wohne in Berlin",losung="wo"))"
os.system("ubung6.save()")
os.system("ubung7= Ubung(frage="'......'  machst du morgen ?Ich werde meine Mutter besuchen",losung="was"))"
os.system("ubung7.save()")
os.system("ubung8= Ubung(frage="dick -- '?'",losung="dünn"))"
os.system("ubung8.save()")
os.system("ubung9= Ubung(frage="voll-'?'",losung="leer"))"
os.system("ubung9.save()")
os.system("ubung10= Ubung(frage="alt-'?'",losung="jung"))"
os.system("ubung10.save()")
os.system("ubung11= Ubung(frage="hungrig-'?'",losung="satt"))"
os.system("ubung11.save()")
os.system("ubung12= Ubung(frage="jung-'?'",losung="alt"))"
os.system("ubung12.save()")
os.system("ubung13= Ubung(frage="schwach--'?'",losung="stark"))"
os.system("ubung13.save()")
os.system("ubung14= Ubung(frage="billig--'?'",losung="teuer"))"
os.system("ubung14.save()")
os.system("ubung15= Ubung(frage="arm--'?'",losung="reich"))"
os.system("ubung15.save()")
os.system("essai1 =Essai(choix = "warum",numf=ubung1))"
essai1.save()
os.system("essai2 =Essai(choix = "wo",numf=ubung1))"
essai2.save()
os.system("essai3 =Essai(choix = "was",numf=ubung1))"
essai3.save()
os.system("essai4 =Essai(choix = "wie",numf=ubung1))"
essai4.save()
os.system("essai1 =Essai(choix = "wie",numf=ubung2))"
essai1.save()
os.system("essai2 =Essai(choix = "wo",numf=ubung2))"
essai2.save()
os.system("essai3 =Essai(choix = "was",numf=ubung2))"
essai3.save()
os.system("essai4 =Essai(choix = "warum",numf=ubung2))"
essai4.save()
os.system("essai1 =Essai(choix = "was",numf=ubung3))"
essai1.save()
os.system("essai2 =Essai(choix = "wo",numf=ubung3))"
essai2.save()
os.system("essai3 =Essai(choix = "wann",numf=ubung3))"
essai3.save()
os.system("essai4 =Essai(choix = "wie",numf=ubung3))"
essai4.save()
os.system("essai1 =Essai(choix = "was",numf=ubung4))"
essai1.save()
os.system("essai2 =Essai(choix = "wann",numf=ubung4))"
essai2.save()
os.system("essai3 =Essai(choix = "wie",numf=ubung4))"
essai3.save()
os.system("essai4 =Essai(choix = "warum",numf=ubung4))"
essai4.save()
os.system("essai5 =Essai(choix = "wer",numf=ubung4))"
essai5.save()
os.system("essai1 =Essai(choix = "wie",numf=ubung5))"
essai1.save()
os.system("essai2 =Essai(choix = "wo",numf=ubung5))"
essai2.save()
os.system("essai3 =Essai(choix = "warum",numf=ubung5))"
essai3.save()
os.system("essai4 =Essai(choix = "wann",numf=ubung5))"
essai4.save()
os.system("essai1 =Essai(choix = "wie",numf=ubung6))"
essai1.save()
os.system("essai2 =Essai(choix = "warum",numf=ubung6))"
essai2.save()
os.system("essai3 =Essai(choix = "was",numf=ubung6))"
essai3.save()
os.system("essai4 =Essai(choix = "wer",numf=ubung6))"
essai4.save()
os.system("essai5 =Essai(choix = "wann",numf=ubung6))"
essai5.save()
os.system("essai1 =Essai(choix = "wer",numf=ubung7))"
essai1.save()
os.system("essai2 =Essai(choix = "wie",numf=ubung7))"
essai2.save()
os.system("essai3 =Essai(choix = "warum",numf=ubung7))"
essai3.save()
os.system("essai4 =Essai(choix = "wo",numf=ubung7))"
essai4.save()
os.system("essai1 =Essai(choix = "schnell",numf=ubung8))"
essai1.save()
os.system("essai2 =Essai(choix = "gesund",numf=ubung8))"
essai2.save()
os.system("essai3 =Essai(choix = "billig",numf=ubung8))"
essai3.save()
os.system("essai4 =Essai(choix = "gesund",numf=ubung8))"
essai4.save()
os.system("essai5 =Essai(choix = "schnell",numf=ubung8))"
essai5.save()
os.system("essai1 =Essai(choix = "leer",numf=ubung9))"
essai1.save()
os.system("essai2 =Essai(choix = "krank",numf=ubung9))"
essai2.save()
os.system("essai3 =Essai(choix = "billig",numf=ubung9))"
essai3.save()
os.system("essai1 =Essai(choix = "dünn",numf=ubung10))"
essai1.save()
os.system("essai2 =Essai(choix = "gesund",numf=ubung10))"
essai2.save()
os.system("essai3 =Essai(choix = "kurz",numf=ubung10))"
essai3.save()
os.system("essai1 =Essai(choix = "voll",numf=ubung11))"
essai1.save()
os.system("essai2 =Essai(choix = "leer",numf=ubung11))"
essai2.save()
os.system("essai3 =Essai(choix = "schlecht",numf=ubung11))"
essai3.save()
os.system("essai1 =Essai(choix = "kurz",numf=ubung12))"
essai1.save()
os.system("essai2 =Essai(choix = "schnell",numf=ubung12))"
essai2.save()
os.system("essai3 =Essai(choix = "heiss",numf=ubung12))"
essai3.save()
os.system("essai1 =Essai(choix = "schlecht",numf=ubung13))"
essai1.save()
os.system("essai2 =Essai(choix = "glücklich",numf=ubung13))"
essai2.save()
os.system("essai3 =Essai(choix = "gut",numf=ubung13))"
essai3.save()
os.system("essai1 =Essai(choix = "warm",numf=ubung14))"
essai1.save()
os.system("essai2 =Essai(choix = "gut",numf=ubung14))"
essai2.save()
os.system("essai3 =Essai(choix = "treu",numf=ubung14))"
essai3.save()
os.system("essai1 =Essai(choix = "langsam",numf=ubung15))"
essai1.save()
os.system("essai2 =Essai(choix = "schmutzig",numf=ubung15))"
essai2.save()
os.system("essai3 =Essai(choix = "traurig",numf=ubung15))"
essai3.save()
