'''

        AUTHOR ZIAD BOUGRINE

'''


import os,sys
DJANGO_SETTINGS_TEMPLATE = "Config/settings.py"
DJANGO_SETTINGS = "germanstudies/settings.py"
DATABASE_USERNAME = "{{username}}"
DATABASE_PASSWORD = "{{password}}"
DATABASE_PORT = "{{port}}"
DATABASE_HOST = "{{locahost}}"
DATABASE_NAME = "{{database}}"






def configureSetting(data):
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



databaseUsername = str(input("Enter Database username:"))
databasePassword = str(input("Enter Database password:"))
databasePort = int(input("Enter Database port:"))
databaseHost = str(input("Enter Database host(Default localhost):"))
databaseName = str(input("Enter Database Name(Default GermanStudies):"))

data = {}
data[DATABASE_USERNAME] = databaseUsername
data[DATABASE_PASSWORD] = databasePassword
data[DATABASE_PORT] = databasePort
data[DATABASE_HOST] = databaseHost
data[DATABASE_NAME] = databaseName

configureSetting(data)