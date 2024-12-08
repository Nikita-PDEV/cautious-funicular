from django.views import View
from django.shortcuts import render
from django.views.generic import CreateView  
from django.contrib.auth.mixins import LoginRequiredMixin  
from .forms import NewsletterSubscriptionForm  
from .models import Newsletter  

class NewsletterSubscriptionView(LoginRequiredMixin, CreateView):  
    model = Newsletter  
    form_class = NewsletterSubscriptionForm  
    template_name = 'newsletter/subscription.html'  
    success_url = '/'  

    def form_valid(self, form):  
        form.instance.user = self.request.user  
        return super().form_valid(form)