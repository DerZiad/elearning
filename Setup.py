'''

        AUTHOR ZIAD BOUGRINE

'''
import os,sys,colorama,time
DJANGO_EMAIL_TEMPLATE = "Config/sender.py"
DJANGO_SETTINGS_TEMPLATE = "Config/settings.py"
DJANGO_EMAIL = "Auth/ValidEntry/sender.py"
DJANGO_SETTINGS = "germanstudies/settings.py"
DATABASE_USERNAME = "{{username}}"
DATABASE_PASSWORD = "{{password}}"
DATABASE_PORT = "{{port}}"
DATABASE_HOST = "{{locahost}}"
DATABASE_NAME = "{{database}}"

EMAIL="{{email}}"
PASSWORD="{{password}}"

class Writer:
    def __init__(self):
        colorama.init()
    def writeSuccess(self, msg):
        return "{} {} {}".format(colorama.Fore.LIGHTGREEN_EX,msg,colorama.Style.RESET_ALL)

    def writeError(self, msg):
        return "{} {} {}".format(colorama.Fore.RED,msg,colorama.Style.RESET_ALL)

    def writeWarning(self, msg):
        return "{} {} {}".format(colorama.Fore.LIGHTYELLOW_EX, msg, colorama.Style.RESET_ALL)

    def writeRequest(self, msg):
        colorama.init()
        return "{} {} {}".format(colorama.Fore.CYAN, msg, colorama.Style.RESET_ALL)

    def writeProposition(self, msg):
        return "{} {} {}".format(colorama.Fore.LIGHTBLUE_EX, msg, colorama.Style.RESET_ALL)

    def writeStep(self, msg):
        return "{} {} {}".format(colorama.Fore.WHITE, msg, colorama.Style.RESET_ALL)
    def writeMessage(self,msg,expression,deisgn=colorama.Fore.WHITE):
        zeit = 0
        theend = ""
        if expression == "word":
            list = msg.split(" ")
            zeit = 0.2
            theend = " "
        elif expression == "letter":
            list = msg
            zeit = 0.1
        else:
            list = msg.split("\n")
            zeit = 0.5
            theend="\n"
        for word in list:
            print("{}{}".format(deisgn,word),end=theend)
            time.sleep(zeit)
        print("{}".format(colorama.Style.RESET_ALL))

wr = Writer()

def configureSetting():
        wr.writeMessage("I m using MySQL database as Database Server , please Give your informations",expression="letter",deisgn=colorama.Fore.LIGHTYELLOW_EX)
        print(wr.writeSuccess("[+] - Recovering Informations"))
        databaseUsername = str(input("====> Enter Database username:"))
        while (len(databaseUsername) == 0):
            print(wr.writeError("I m sorry but username should be at least 1 character"))
            databaseUsername = str(input("====> Enter Database username:"))
        databasePassword = str(input("====> Enter Database password:"))
        while(len(databasePassword) == 0):
            print(wr.writeError("I m sorry but username should be at least 1 character"))
            databasePassword = str(input("====> Enter Database password:"))
        databasePort = str(input("====> Enter Database port(Default 3306, Press Enter):"))
        databaseHost = str(input("====> Enter Database host(Default localhost, Press Enter):"))
        databaseName = str(input("====> Enter Database Name(Default GermanStudies, Press Enter):"))

        if(len(databaseHost)==0):
            databaseHost = "localhost"
        if(len(databasePort) == 0):
            databasePort = "3306"
        if(len(databaseName)==0):
            databaseName = "GermanStudies"
        print(wr.writeSuccess("[+] - Configuring Django Settings"))
        fileSetting = open(DJANGO_SETTINGS_TEMPLATE, mode="r", encoding="utf-8")
        settings = fileSetting.read()
        settings = settings.replace(DATABASE_USERNAME,databaseUsername)
        settings = settings.replace(DATABASE_PASSWORD, databasePassword)
        settings = settings.replace(DATABASE_PORT, databasePort)
        settings = settings.replace(DATABASE_HOST, databaseHost)
        settings = settings.replace(DATABASE_NAME,databaseName)
        fileSetting.close()
        replateSetting = open(DJANGO_SETTINGS,mode="w",encoding="UTF-8")
        replateSetting.write(settings)
        replateSetting.close()
def configuringSMTP():
    wr.writeMessage("I m using SMTP Service as Mailing service to email verification action..., please Give your informations email and password and please be carefull", expression="letter",
                    deisgn=colorama.Fore.LIGHTYELLOW_EX)
    wr.writeMessage("Please go to gmail security and go down you will find allow strange application, allow it(change it to yes)",
        expression="letter",
        deisgn=colorama.Fore.RED)
    print(wr.writeSuccess("[+] - Recovering SMTP Informations"))
    emailAtt = str(input("====> Enter Gmail Email:"))
    while (len(emailAtt) == 0):
        print(wr.writeError("I m sorry but email should be correct"))
        emailAtt = str(input("====> Enter Gmail Email:"))
    passwordAtt = str(input("====> Enter Gmail password:"))
    while (len(passwordAtt) == 0):
        print(wr.writeError("I m sorry but email should be correct"))
        passwordAtt = str(input("====> Enter Gmail password:"))
    print(wr.writeSuccess("[+] - Configuring Django Mailing"))
    emailSender = open(DJANGO_EMAIL_TEMPLATE, mode="r", encoding="utf-8")
    emailSenderMessage = emailSender.read()
    emailSenderMessage = emailSenderMessage.replace(EMAIL, emailAtt)
    emailSenderMessage = emailSenderMessage.replace(PASSWORD, passwordAtt)
    emailSender.close()
    replateSetting = open(DJANGO_EMAIL, mode="w", encoding="UTF-8")
    replateSetting.write(emailSenderMessage)
    replateSetting.close()
def installRequirement():
    print(wr.writeWarning("[+] - Installing Requirements"))
    os.system("pip install -r requirements.txt")
    wr.writeMessage("Hey bro again , if you re in this step that means that the package is succesfully installed,let's move to the next Step",expression="letter",deisgn=colorama.Fore.LIGHTBLUE_EX)
print("#####################################################################################################")
print()
print()
print()

wr.writeMessage("The website is for learning germany please follow the step in the script to install it successfully",expression="word",deisgn=colorama.Fore.CYAN)
print()
print()
wr.writeMessage("This Server is using MySql as database and Anaconda as package library",expression="letter",deisgn=colorama.Fore.RED)
print()
wr.writeMessage("Hi friend, I m ziad , i m presenting you our project , i will guid you in installing the website on your machine",expression="letter",deisgn=colorama.Fore.LIGHTMAGENTA_EX)


installRequirement()

configureSetting()

configuringSMTP()

print()
print()
wr.writeMessage("Congrats my friend, let's run the website together now",expression="letter",deisgn=colorama.Fore.LIGHTMAGENTA_EX)
os.system("python manage.py runserver")