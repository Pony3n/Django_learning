from django import forms
from app_media.models import *

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=500)
    file = forms.FileField()

class DocumentForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('description', 'file')

class MultiFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})) #Возможность загрузки нескольких файлов