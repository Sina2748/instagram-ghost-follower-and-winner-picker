# books/urls.py
from django.urls import path
from .views import pick_view, win_view, free_pick_view

urlpatterns = [
    path('pick/', pick_view, name='pick'),
    path('pick/winners/', win_view, name='win'),
    path('free_pick/', free_pick_view, name='free_pick'),

]