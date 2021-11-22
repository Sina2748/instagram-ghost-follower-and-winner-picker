# books/urls.py
from django.urls import path
from .views import pick_view, win_view

urlpatterns = [
    path('pick/', pick_view, name='pick'),
    path('pick/winners/', win_view, name='win'),

]