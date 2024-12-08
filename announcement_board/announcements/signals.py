from django.db.models.signals import post_save  
from django.dispatch import receiver  
from .models import Reply  
from django.core.mail import send_mail  

@receiver(post_save, sender=Reply)  
def send_reply_notification(sender, instance, created, **kwargs):  
    if created:  
        # Отправка email уведомления пользователю, оставившему отклик  
        send_mail(  
            'New Reply',  
            f'You have a new reply on your announcement: {instance.announcement.title}',  
            'from@example.com',  
            [instance.announcement.user.email],  
            fail_silently=False,  
        )  

@receiver(post_save, sender=Reply, condition=lambda instance: instance.is_accepted)  
def send_accepted_reply_notification(sender, instance, **kwargs):  
    # Отправка email уведомления пользователю, оставившему принятый отклик  
    send_mail(  
        'Reply Accepted',  
        f'Your reply on the announcement "{instance.announcement.title}" has been accepted.',  
        'from@example.com',  
        [instance.user.email],  
        fail_silently=False,  
    )