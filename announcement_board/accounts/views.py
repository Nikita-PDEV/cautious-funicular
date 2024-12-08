from django.conf import settings
from django.core.mail import send_mail
from django.views import View
from django.contrib.auth import authenticate, login, logout  
from django.shortcuts import render, redirect  
from .forms import RegistrationForm, LoginForm  
from .models import RegistrationCode, User  

class RegisterView(View):  
    def get(self, request):  
        form = RegistrationForm()  
        return render(request, 'registration/register.html', {'form': form})  

    def post(self, request):  
        form = RegistrationForm(request.POST)  
        if form.is_valid():  
            user = form.save(commit=False)  
            user.is_active = False  
            user.username = user.email.split("@")[0]
            user.save()  
            registration_code = RegistrationCode.objects.create(user=user)  

            send_mail(
                subject="Код активации",
                message=f"Используйте код для активации аккаунта: {registration_code.code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )
            return redirect('confirm_registration')  
        return render(request, 'registration/register.html', {'form': form})  

class ConfirmRegistrationView(View):  
    def get(self, request):  
        return render(request, 'registration/confirm_registration.html')  

    def post(self, request):  
        code = request.POST.get('code')  
        try:  
            registration_code = RegistrationCode.objects.get(code=code)  
            if registration_code.user.is_active:  # Проверка, активирован ли пользователь
                return render(request, 'registration/confirm_registration.html', {'error': 'User is already active.'})
            registration_code.user.is_active = True  
            registration_code.user.save()  
            # Можно отметить код как использованный, если нужно
            registration_code.delete()  # Удаляем код после использования
            login(request, registration_code.user)  
            return redirect('announcement_list')  
        except RegistrationCode.DoesNotExist:  
            return render(request, 'registration/confirm_registration.html', {'error': 'Invalid code'})  

class LoginView(View):  
    def get(self, request):  
        form = LoginForm()  
        return render(request, 'registration/login.html', {'form': form})  

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('announcement_list')
        else:
            form = LoginForm()
            return render(request, 'registration/login.html', {'form': form, 'error': 'Неверный логин или пароль'})

class LogoutView(View):  
    def get(self, request):  
        logout(request)  
        return redirect('login')