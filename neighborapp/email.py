from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to Myneighborhood'
    sender = 'devcoderdeveloper65@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/newsemail.txt',{"name": name})
    html_content = render_to_string('email/newsemail.html',{"name": name})

    msg = send_mail(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()