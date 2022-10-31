from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_media.models import *
from app_media.forms import *

def upload_file(request):
    if request.method == 'POST':            #Если данные пришли от клиента
        upload_file_form = UploadFileForm(request.POST, request.FILES)      #Создаем объект с файлом
        if upload_file_form.is_valid():         #Проверяем валидность данных
            file = request.FILES['file']        #Присваиваем переменную файлу
            return HttpResponse(content=file.name, status=200)    #Возвращаем результат
    else:
        upload_file_form = UploadFileForm()     #Возвращаем пустую страницу

    context = {'form': upload_file_form}
    return render(request, 'app_media/upload_file.html', context=context)

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'app_media/file_form_upload.html', {'form': form})

def multi_model_form_upload(request):
    if request.method == 'POST':
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)         #представляем через объект модели File
                instance.save()
            return redirect('/')
    else:
        form = MultiFileForm()
    return render(request, 'app_media/upload_files.html', {'form': form})

