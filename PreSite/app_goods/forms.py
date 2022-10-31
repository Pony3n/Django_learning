from django import forms

class UpLoadPriceForm(forms.Form):
    file = forms.FileField()