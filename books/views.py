from django.shortcuts import render

# Create your views here.
# books/views.py
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list' # new
    template_name = 'books/book_list.html'

class BookDetailView(DetailView): # new
    model = Book
    context_object_name = 'book' # new
    template_name = 'books/book_detail.html'