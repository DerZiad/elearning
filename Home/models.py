from django.db import models
from Auth.models import Personne
# Create your models here.
from time import *
import threading
import Home.timer as timer
import threading


class Message(models.Model):

    message = models.TextField()
    subject = models.TextField()
    personne = models.ForeignKey(Personne,on_delete=models.CASCADE)
'''
def countup():
    i = 0
    global my_timer
    while(i==0):
        my_timer = 5

        for x in range(86400):
            sleep(1)
        messages = Message.objects.all()
        for message in messages:
            message.delete()

threadforum = threading.Thread(target=countup)
threadforum.start()
'''