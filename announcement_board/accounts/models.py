from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin  
from django.db import models  
import random
import string

class UserManager(BaseUserManager):  
    def create_user(self, email, password=None, **extra_fields):  
        if not email:  
            raise ValueError('The Email field must be set')  
        email = self.normalize_email(email)  
        user = self.model(email=email, **extra_fields)  
        user.set_password(password)  
        user.save(using=self._db)  
        return user  

    def create_superuser(self, email, password, **extra_fields):  
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  
        return self.create_user(email, password, **extra_fields)  

class User(AbstractUser, PermissionsMixin):  
    email = models.EmailField(unique=True)  
    is_active = models.BooleanField(default=False)  
    is_staff = models.BooleanField(default=False)  

    objects = UserManager()  

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  

    def __str__(self):  
        return self.email  

def gen_code():
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return code

class RegistrationCode(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    code = models.CharField(max_length=6, unique=True, default=gen_code())  
    created_at = models.DateTimeField(auto_now_add=True)  