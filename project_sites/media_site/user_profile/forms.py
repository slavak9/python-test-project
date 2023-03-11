from django.forms import ModelForm, TextInput,ImageField
from user_profile.models import Usermodel
from django import forms

class User_form(ModelForm):
    class Meta:
        model = Usermodel
        fields = ['name','last_name','city','photo']

        widgets = {
            'name': TextInput(attrs={'class': 'comment', 'placeholder': 'Enter your name'}),
            'last_name': TextInput(attrs={'class': 'comment', 'placeholder': 'Enter your last_name'}),
            'city': TextInput(attrs={'class': 'comment', 'placeholder': 'Enter your city'}),
            # 'photo': ImageField()
        }