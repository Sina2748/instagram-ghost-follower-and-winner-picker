from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Create your views here.
# books/views.py
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import insta_model
from .forms import AddCreateForm
import instaloader
import random

# Create your views here.
def win_view(request):
    context = {}
    form = AddCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # save the form data to model
        print('hi3')
        form.save()
        # print(form)
        
        book_list = insta_model.objects.all()
        # print(book_list)

        context= {'book_list':book_list}
        # print(context)

        a = insta_model.objects.values( 'insta_url', 'picker_kind', 'number_of_winers' )
        b = a[len(a)-1]
        user_insta_url_str = b["insta_url"]

        picker_kind = b["picker_kind"]
        number_of_winers = b["number_of_winers"]

        print(picker_kind)
        print(number_of_winers)

        PROFILE = "anis2423g"
        SHORTCODE = user_insta_url_str[28:39]
        print(SHORTCODE)
               
        L = instaloader.Instaloader()

        # Load session previously saved with `instaloader -l USERNAME`:
        L.login("anis2423g", "anisanisanis") 
        # USER = "anis2423f"
        # L.load_session_from_file(USER)
        profile = instaloader.Profile.from_username(L.context, PROFILE)

        likes = []
        comments_from_loop = []
        the_winner_list = []

        ### comments
        if picker_kind == 'comments':            
            print("Fetching comments of all posts of profile {}.".format(SHORTCODE))
            for post in profile.get_posts():
                post2 = post.from_shortcode(L.context, SHORTCODE)
                for x in post2.get_comments():
                    comments_from_loop.append(x.owner)
            print(comments_from_loop)
            
            # clearing list comments_from_loop
            a = []
            c = []
            for x in comments_from_loop:
                a = str(x)
                b = a[9:-14]
                c.append(b)    

            comments_from_loop = c
            the_winner_list = comments_from_loop

        ### likes
        elif picker_kind == 'likes':        
            print("Fetching likes of all posts of profile {}.".format(SHORTCODE))
            for post in profile.get_posts():
                likes = post.from_shortcode(L.context, SHORTCODE).get_likes()
                
            ran_like = []
            for like in likes:
                ran_like = ran_like + [like.username]

            print(ran_like)
            the_winner_list = ran_like

        ### mentions
        elif picker_kind == 'mentions':
            pass
        

        winner = random.sample(the_winner_list, int(number_of_winers))
        print("winner is {}".format(winner))

        context= {'winner':winner}
        # print(context)

        return render(request, "about.html", context)
    
    # context ={}
    # context['form']= ["No winners!"]
    return render(request, "about.html")


def pick_view(request):
    context ={}
    print("hi1")
    # create object of form
    form = AddCreateForm(request.POST or None, request.FILES or None)
      


    print('hi2')
    context['form']= form
    # print(context['form'])
    return render(request, "insta_app_templates/add.html", context)