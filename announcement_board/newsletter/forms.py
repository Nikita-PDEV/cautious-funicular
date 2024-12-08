from django import forms  
from .models import Newsletter  

class NewsletterSubscriptionForm(forms.ModelForm):  
    class Meta:  
        model = Newsletter  
        fields = ['user']