from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserLog, UserRole
from django.core.mail import send_mail

@receiver(post_save, sender=UserRole)
def send_email_on_user_creation(sender, instance, created, **kwargs):
    if created:
        subject = 'User credentials!'
        message = f'user name : {instance.user} and password : {instance.password}'
        from_email = 'exmp@gmail.com'
        to_email = ["exmp@gmail.com"]
        send_mail(subject, message, from_email, to_email)
