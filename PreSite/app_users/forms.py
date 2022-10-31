from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ExtendedRegisterForm(UserCreationForm):       #Расширяем форму регистрации
    nickname = forms.CharField(max_length=30, required=False, help_text='Ник')
    first_name = forms.CharField(max_length=30,required=False, help_text='Имя')
    second_name = forms.CharField(max_length=30,required=False, help_text='Фамилия')
    city = forms.CharField(max_length=30, required=False, help_text='Город')
    date_of_birth = forms.DateField(required=False, input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'second_name', 'password1', 'password2', 'nickname', 'date_of_birth')    #Поля, которые будут отображаться