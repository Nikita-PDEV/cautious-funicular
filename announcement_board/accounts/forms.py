from django import forms  
from django.contrib.auth.forms import AuthenticationForm  
from .models import User, RegistrationCode  

class RegistrationForm(forms.ModelForm):  

    class Meta:  
        model = User  
        fields = ['email', 'password']  

    def save(self, commit=True):  
        user = super().save(commit=False)  
        user.set_password(self.cleaned_data['password'])  
        if commit:  
            user.save()  
        return user  

class LoginForm(AuthenticationForm):  
    pass