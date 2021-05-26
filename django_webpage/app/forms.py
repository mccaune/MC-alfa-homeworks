from django import forms
from .models import Countries
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CountryForm1(forms.ModelForm):
    class Meta:
        model = Countries
        fields = ['name', 'country_code2', 'country_code3', 'area', 'region']
        labels = {
            'name': 'Nosaukums', 
            'country_code2': 'Kods(2)', 
            'country_code3': 'Kods(3)', 
            'area': 'Platība', 
            'region': 'Reģions',
        }
    

