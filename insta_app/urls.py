# books/urls.py
from django.urls import path
from .views import add_view, win_view

urlpatterns = [
    path('add/', add_view, name='add'),
    path('add/winners/', win_view, name='win'),

]