# books/urls.py
from django.urls import path
from .views import pick_view, win_view, free_pick_view, ghost_followers_view, ghosts_are_view

urlpatterns = [
    path('pick/', pick_view, name='pick'),
    path('pick/winners/', win_view, name='win'),
    path('free_pick/', free_pick_view, name='free_pick'),
    path('ghost_followers/', ghost_followers_view, name='ghost_followers'),
    path('ghosts_are/', ghosts_are_view, name='ghosts_are'),

]