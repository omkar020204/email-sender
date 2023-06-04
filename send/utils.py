from django.core.mail import send_mail
from django.conf import settings
def send_email_to_client(title,message,email):
    from_mail=settings.EMAIL_HOST_USER
    mail = list(email.split(" "))
    send_mail(title,message,'omkarsk0202@gmail.com',mail)
