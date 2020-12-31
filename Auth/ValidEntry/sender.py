import smtplib
from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template import loader
def sendEmail(infos,request):
        mail_content = infos['text']
        #The mail addresses and password
        sender_address = 'germanlernen398@gmail.com'
        sender_pass = 'xihtcsbsodpyfipc'
        receiver_address = infos['address']

        context = {
            'textcontent':mail_content
        }
        template = loader.get_template("letter/letter.html")
        html = template.render(context)
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = infos['subject']   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(html, 'html'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()