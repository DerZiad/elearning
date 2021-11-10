'''

        AUTHOR ZIAD BOUGRINE

'''
import os,sys,colorama


DJANGO_SETTINGS_TEMPLATE = "Config/settings.py"
DJANGO_SETTINGS = "germanstudies/settings.py"
DATABASE_USERNAME = "{{username}}"
DATABASE_PASSWORD = "{{password}}"
DATABASE_PORT = "{{port}}"
DATABASE_HOST = "{{locahost}}"
DATABASE_NAME = "{{database}}"




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

def configureSetting():
        wr = Writer()
        print(wr.writeSuccess("[+] - Recovering Informations"))
        databaseUsername = str(input("====> Enter Database username:"))
        databasePassword = str(input("====> Enter Database password:"))
        databasePort = int(input("====> Enter Database port:"))
        databaseHost = str(input("====> Enter Database host(Default localhost):"))
        databaseName = str(input("====> Enter Database Name(Default GermanStudies):"))

        data = {}
        data[DATABASE_USERNAME] = databaseUsername
        data[DATABASE_PASSWORD] = databasePassword
        data[DATABASE_PORT] = databasePort
        data[DATABASE_HOST] = databaseHost
        data[DATABASE_NAME] = databaseName

        print("[+] - Configuring Django Settings")
        fileSetting = open(DJANGO_SETTINGS_TEMPLATE, mode="r", encoding="utf-8")
        settings = fileSetting.read()
        settings = settings.replace(DATABASE_USERNAME,data[DATABASE_USERNAME])
        settings = settings.replace(DATABASE_PASSWORD, data[DATABASE_PASSWORD])
        settings = settings.replace(DATABASE_PORT, str(data[DATABASE_PORT]))
        settings = settings.replace(DATABASE_HOST, data[DATABASE_HOST])
        settings = settings.replace(DATABASE_NAME,data[DATABASE_NAME])
        fileSetting.close()
        replateSetting = open(DJANGO_SETTINGS,mode="w",encoding="UTF-8")
        replateSetting.write(settings)
        replateSetting.close()

def installRequirement():
        print("[+] - Installing Requirements")
        os.system("pip install -r requirements.txt")

configureSetting()
installRequirement()

