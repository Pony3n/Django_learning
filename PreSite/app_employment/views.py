from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from app_employment.models import *


# def vacancy_list(request):
    # if request.user.has_perm('app_employment.view_vacancy'):     #Django проверяет есть ли у пользователя права (метод has_perm) #<app>.<action>_<object_name>
    #     vacancies = Vacancy.objects.all()
    #     return render(request, 'app_employment/vacancy_list.html', {'vacancy_list': vacancies})
    # else:
    #     raise PermissionDenied()
    #
    # Но лучше:
    #
    # if not request.user.has_perm('app_employment.view_vacancy'):
    #     raise PermissionDenied()
    # vacancies = Vacancy.objects.all()
    # return render(request, 'app_employment/vacancy_list.html', {'vacancy_list': vacancies})

    #Еще лучше через декоратор:

@permission_required('app_employment.view_vacancy')
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'app_employment/vacancy_list.html', {'vacancy_list': vacancies})