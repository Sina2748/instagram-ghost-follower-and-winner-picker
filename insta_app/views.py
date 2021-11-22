from django.shortcuts import render
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



def add_view(request):
    context ={}
    print("hi1")
    # create object of form
    form = AddCreateForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
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
        user_insta_ID_str = b["insta_url"]
        picker_kind = b["picker_kind"]
        number_of_winers = b["number_of_winers"]

        print(picker_kind)
        print(number_of_winers)

        if picker_kind == 'comments':
            pass
        elif picker_kind == 'likes':

            PROFILE = "anis2423g"
            SHORTCODE = user_insta_ID_str

            L = instaloader.Instaloader()

            # Load session previously saved with `instaloader -l USERNAME`:
            L.login("anis2423g", "anisanisanis") 
            # USER = "anis2423f"
            # L.load_session_from_file(USER)
            profile = instaloader.Profile.from_username(L.context, PROFILE)

            likes = []
            print("Fetching likes of all posts of profile {}.".format(SHORTCODE))
            for post in profile.get_posts():
                likes = post.from_shortcode(L.context, SHORTCODE).get_likes()
                print(likes)

            ran_like = []
            for like in likes:
                ran_like = ran_like + [like.username]

            print(ran_like)
            winner = random.sample(ran_like, int(number_of_winers))
            print("winner is {}".format(winner))

        elif picker_kind == 'mentions':
            pass



        #### instaloader ####   
        # L = instaloader.Instaloader()
        # # user_insta_ID = insta_model.objects.last()
        # # user_insta_ID_str = str(user_insta_ID)
        
        # PROFILE = user_insta_ID_str

        # # Load session previously saved with `instaloader -l USERNAME`:
        # L.login("anis2423f", "anisanisanis") 
        # # USER = "anis2423f"
        # # L.load_session_from_file(USER, " ~\books\insta_app\session-anis2423f ")

        # profile = instaloader.Profile.from_username(L.context, PROFILE)

        # likes = []
        # print("Fetching likes of all posts of profile {}.".format(profile.username))
        # for post in profile.get_posts():
        #     print(post)
        #     likes = likes + list(post.get_likes())

        # print("Storing like into file.")
        # with open("inactive-users.txt", 'w') as f:
        #     for like in likes:
        #         print(like.username, file=f)


        # likes = set()
        # print("Fetching likes of all posts of profile {}.".format(profile.username))
        # for post in profile.get_posts():
        #     print(post)
        #     likes = likes | set(post.get_likes())     
        
        ####################

        book_list = insta_model.objects.all()
        # print(book_list)
        context= {'book_list':book_list}
        # print(context)

        context['variable']= book_list
        return render(request, "about.html", {'book_list':book_list})

    print('hi2')
    context['form']= form
    # print(context)
    return render(request, "insta_app_templates/add.html", context)