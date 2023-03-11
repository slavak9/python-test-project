from django import forms
from django.core.exceptions import ValidationError


class Add_Models_forms_manualy(forms.Form):
    title = forms.CharField(max_length=210,widget=forms.TextInput(attrs={'class': 'comment','placeholder':'Enter title'}))
    post = forms.CharField(widget=forms.Textarea(attrs={'class': 'comment','placeholder':'Describe your post'}))
    media_file = forms.FileField(required=False,widget=forms.FileInput(attrs={'name':'myfile','id':'myfile'}))

    # type_file = forms.CharField(max_length=100)

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(str(title)) > 200:
    #
    #         raise ValidationError('The length more than 255 simbols')
    #     return title

