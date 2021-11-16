# https://www.agiliq.com/blog/2019/01/django-createview/
from .models import Book
from django import forms
from django.forms import ModelForm

class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']

