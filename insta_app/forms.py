# https://www.agiliq.com/blog/2019/01/django-createview/
from .models import insta_model, insta_ghost_model
from django import forms
from django.forms import ModelForm

class AddCreateForm(forms.ModelForm):
    class Meta:
        model = insta_model
        fields = "__all__"


class FreeAddCreateForm(forms.ModelForm):
    class Meta:
        model = insta_model
        fields = "__all__"
        exclude = ['number_of_winers']

class AddCreateGhostForm(forms.ModelForm):
    class Meta:
        model = insta_ghost_model
        fields = "__all__"

# class AddCreateGhostForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)