from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_users.forms import *
from app_users.models import Profile

def login_view(request):
    if request.method == 'POST':        #Для POST пытается аутентифицировать пользователя
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)   #Эта функиця принимает (логи, пароль) и проверяет наличие пользователя в БД пользователей
            if user:                                                    #Вернет объект пользователя или None
                if user.is_active:                  #Проверяем активен ли пользователь
                    login(request,user)             #Функцмя принимает request и user -> устанавливает сессию пользователя
                    return HttpResponse('вы успешно зашли')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Пользователь не активен')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина и пароля')
    else:           #Для остальных случаев отображаем форму регистрации
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'app_users/login.html', context=context)

class AnotherLoginView(LoginView):      #Создание класса представления для Логина
    template_name = 'app_users/login.html'

def logout_view(request):
    logout(request)         #При вызове logout Django сам деает всю магию
    return HttpResponse("Вы успешно вышли из своей учетной записи")

class AnotherLogOut(LogoutView):
    template_name = 'app_users/logout.html'
#    next_page = '/'     #Redirect


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)       #Форма создания пользователя от Django
        if form.is_valid():
            form.save()         #Сохраняем пользователя
            username = form.cleaned_data.get('username')            #Этот блок кода после save -автоматическая аутентификация пользователя сразу после регистрации
            raw_password = form.cleaned_data.get('password1')       #Password1: первоначальный пароль. Password2: потвторение пароля
            user = authenticate(username=username, password=raw_password)   #Пароли Django хранит через хэш-функции
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'app_users/register.html', {'form': form})

def another_register_view(request):
    if request.method == 'POST':
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            nickname = form.cleaned_data.get('nickname')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth,
                nickname=nickname               #Сохранение объекта в БД
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = ExtendedRegisterForm()
    return render(request, 'app_users/register.html', {'form': form})