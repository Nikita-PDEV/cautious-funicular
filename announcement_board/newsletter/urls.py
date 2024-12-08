from django.urls import path  
from . import views  

urlpatterns = [  
    path('subscribe/', views.NewsletterSubscriptionView.as_view(), name='newsletter_subscribe'),  
]