from django.db.models.signals import post_save  
from django.dispatch import receiver  
from .models import Newsletter  
from django.core.mail import send_mail  
from django.conf import settings  

@receiver(post_save, sender=Newsletter)  
def send_newsletter_email(sender, instance, created, **kwargs):  
    if created:  
        subject = "New Newsletter Subscription"  
        message = f"A new user ({instance.user.email}) has subscribed to the newsletter."  
        from_email = settings.DEFAULT_FROM_EMAIL  
        recipient_list = [admin_email for admin_email in settings.ADMINS]  
        
        send_mail(  
            subject=subject,  
            message=message,  
            from_email=from_email,  
            recipient_list=recipient_list,  
            fail_silently=False,  
        )