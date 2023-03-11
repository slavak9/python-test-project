from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from main.models import Comments

class Comments_form(ModelForm):
    class Meta(Comments):
        model = Comments
        fields = ['comment']

        widgets = {
            'name': TextInput(attrs={'class': 'comment', 'placeholder': 'Enter your name'}),
            'comment': Textarea(attrs={'class': 'comment', 'placeholder': 'Enter your comment'})
                   }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(args, kwargs)
        #     self.cleaned_data = None
        #
        # def clean_name(self):
        #     name = self.cleaned_data['name']
        #     if len(name) > 45:
        #
        #         raise ValidationError('The length more than 255 simbols')
        #     return name

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'comment', 'placeholder': 'Enter your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'comment', 'placeholder': 'Enter your email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'comment', 'placeholder': 'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'comment', 'placeholder': 'Repeat your password'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Login_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'comment', 'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'comment', 'placeholder': 'Enter your password'}))

