from _csv import reader
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render
from app_goods.models import *
from app_goods.forms import *

def items_list(request):
    items = Item.objects.all()
    return render(request, 'app_goods/item_list.html', context={'item_list': items})

def update_price(request):
    if request.method == 'POST':        #Получаем файл
        upload_file_form = UpLoadPriceForm(request.POST, request.FILES)    #Создаем объект по форме
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()       #Считываем файл
            price_str = price_file.decode('utf-8').split('\n')      #вычленяем цены
            csv_reader = reader(price_str, delimiter=',', quotechar='' '')  #Преобразуем в csv
            for row in csv_reader:
                Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))  #Обновляем данные
            return HttpResponse(content='Цены успешно обновлены', status=200)
    else:
        upload_file_form = UpLoadPriceForm()

    context = {'form': upload_file_form}

    return render(request, 'app_media/upload_file.html')
