from django.urls import path  
from django.views import View  
from . import views 

urlpatterns = [  
    path('register/', views.RegisterView.as_view(), name='register'),  
    path('confirm_registration/', views.ConfirmRegistrationView.as_view(), name='confirm_registration'),  
    path('login/', views.LoginView.as_view(), name='login'),  
    path('logout/', views.LogoutView.as_view(), name='logout'),  
]