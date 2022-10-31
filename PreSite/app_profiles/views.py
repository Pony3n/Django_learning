from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import User
from .forms import *


def main(request):
    return render(request, 'profiles/hello.html')


class UserFormView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request, 'profiles/register.html', {'user_form': user_form})

    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'profiles/register.html', {'user_form': user_form})

