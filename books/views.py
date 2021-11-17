from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Create your views here.
# books/views.py
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import Book
from .forms import BookCreateForm

# https://www.agiliq.com/blog/2019/01/django-createview/

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list' # new
    template_name = 'books/book_list.html'

class BookDetailView(DetailView): # new
    model = Book
    context_object_name = 'book' # new
    template_name = 'books/book_detail.html'

def home_view(request):
    context ={}
    print("hi3")
    # create object of form
    form = BookCreateForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        print('hi1')
        form.save()
        print(form)
        
        book_list = Book.objects.all()
        print(book_list)
        context= {'book_list':book_list}
        print(context)
        # context['variable']= book_list
        return render(request, "about.html", {'book_list':book_list})

    print('hi2')
    context['form']= form
    print(context)
    return render(request, "books/add.html", context)

# class BookCreateView(CreateView): # new
#     # model = Book
#     # fields = ('title', 'author', 'price')
#     # template_name = 'books/add.html'
#     def get(self, request, *args, **kwargs):
#         context = {'form': BookCreateForm()}
#         return render(request, 'books/add.html', context)

    # def post(self, request, *args, **kwargs):
    #     form = BookCreateForm(request.POST)
    #     if form.is_valid():
    #         book = form.save()
    #         book.save()
    #         return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
    #     return render(request, 'books/add.html', {'form': form})

# import Http Response from django
from django.http import HttpResponse
# get datetime
import datetime
 
# create a function
def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)