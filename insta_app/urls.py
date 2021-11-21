# books/urls.py
from django.urls import path
from .views import add_view

urlpatterns = [
    path('add/', add_view, name='add'),

]