from django import forms  
from .models import Announcement, Reply  

class AnnouncementForm(forms.ModelForm):  
    class Meta:  
        model = Announcement  
        fields = ['title', 'content', 'category']  

class ReplyForm(forms.ModelForm):  
    class Meta:  
        model = Reply  
        fields = ['content']