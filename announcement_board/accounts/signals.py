from django.db.models.signals import post_save  
from django.dispatch import receiver  
from .models import RegistrationCode, User  
from django.core.mail import send_mail  

@receiver(post_save, sender=RegistrationCode)  
def send_confirmation_email(sender, instance, created, **kwargs):  
    if created:  
        # Отправка email с кодом подтверждения  
        send_mail(  
            'Confirmation Code',  
            f'Your confirmation code is: {instance.code}',  
            'from@example.com',  
            [instance.user.email],  
            fail_silently=False,  
        )  

@receiver(post_save, sender=User)  
def add_to_newsletter(sender, instance, created, **kwargs):  
    if created and instance.is_active:  
        # Добавление пользователя в список для новостной рассылки  
        Newsletter.objects.create(user=instance)