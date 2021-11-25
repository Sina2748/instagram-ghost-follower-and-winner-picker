# https://www.agiliq.com/blog/2019/01/django-createview/
from .models import insta_model
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

