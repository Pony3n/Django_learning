from django.shortcuts import render
from django.http import HttpResponse
from django.views import View, generic
from django.views.generic import TemplateView

from .models import *

def adv_list(request):
    adv = Advertisment.objects.all()
    return render(request, 'Alphachanel/advertisement.html', {'adv': adv})


def main_chanel_1(request):
    return HttpResponse('<ul>'
                        '<li>Фантазер на час</li>'
                        '<li>Монтажер на час</li>'
                        '<li>Услуги отбойника по ссылке</li>'
                        '</ul>')

def main_chanel(request):
    return render(request, 'Alphachanel/main_chanel.html')

def second_chanel(request):
    return render(request, 'Alphachanel/second_chanel.html')

def third_chanel(request):
    return render(request, 'Alphachanel/new_href_training.html')

def fourth_chanel(request):
    sentence_list = ['Фантазер на час',
                     'Монтажер на час',
                     'Услуги отбойника по ссылке']
    return render(request, 'Alphachanel/sentence_list.html', {'sentence_list': sentence_list})

def contacts(request):
    contact_list = {'John': ['8-964-876-27-85', 'root@toor.ru'],
                    'Anna': ['8-964-876-27-85', 'root@toor.ru'],
                    'Misha': ['8-964-876-27-85', 'root@toor.ru']}
    return render(request, 'Alphachanel/contacts.html', {'contact_list': contact_list})

def about(request):
    about_company = {'Voennaya': 'Очень пиздатая компания',
                     'Ne Voennaya': 'Не Очень пиздатая компания',
                     'Okolo Voennaya': 'Около Очень пиздатая компания',
                     'Pochti Voennaya': 'Почти Очень пиздатая компания'}
    return render(request, 'Alphachanel/about.html', {'about': about_company})

class About_1(View):
    def get(self, request):
        regions = ['region_1', 'region_2', 'region_3', 'region_4', 'region_5']
        return render(request, 'Alphachanel/regions.html', {'regions': regions})

    def post(self):
        print('успешно создан')

class About(TemplateView):
    template_name = 'Alphachanel/regions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Регионы, которые вас интересуют'
        context['title'] = 'Регионы'
        context['description']= ''''
        Много текста о регионах, которые вы можете увидеть здесь!
        '''
        return context



class AdvertismentListView(generic.ListView):
    model = Advertisment
    template_name = 'advertisment_list.html'