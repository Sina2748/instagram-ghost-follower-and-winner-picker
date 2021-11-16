from django.shortcuts import render

# Create your views here.
# books/views.py
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list' # new
    template_name = 'books/book_list.html'

class BookDetailView(DetailView): # new
    model = Book
    context_object_name = 'book' # new
    template_name = 'books/book_detail.html'

class BookCreateView(CreateView): # new
    model = Book
    fields = ('title', 'author', 'price')
    template_name = 'books/add.html'