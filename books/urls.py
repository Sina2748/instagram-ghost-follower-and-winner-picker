# books/urls.py
from django.urls import path
from .views import BookListView, BookDetailView
from .views import geeks_view, home_view

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'), # new
    # path('add/', BookCreateView.as_view(), name='add'),
    path('geek/', geeks_view),
    path('add/', home_view),

]