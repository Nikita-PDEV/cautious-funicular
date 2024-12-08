from django.db import models  
from accounts.models import User  

class Announcement(models.Model):  
    CATEGORIES = (  
        ('tanks', 'Танки'),  
        ('healers', 'Хилы'),  
        ('dd', 'ДД'),  
        ('traders', 'Торговцы'),  
        ('guildmasters', 'Гилдмастеры'),  
        ('questgivers', 'Квестгиверы'),  
        ('blacksmiths', 'Кузнецы'),  
        ('leatherworkers', 'Кожевники'),  
        ('alchemists', 'Зельевары'),  
        ('mages', 'Мастера заклинаний'),  
    )  

    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    category = models.CharField(max_length=20, choices=CATEGORIES)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

class Reply(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    is_accepted = models.BooleanField(default=False)