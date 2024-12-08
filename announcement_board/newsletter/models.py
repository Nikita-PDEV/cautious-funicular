from django.db import models  
from accounts.models import User  

class Newsletter(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    subscribed_at = models.DateTimeField(auto_now_add=True)