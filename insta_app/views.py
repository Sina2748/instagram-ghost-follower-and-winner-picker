from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Create your views here.
# books/views.py
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import insta_model
from .forms import AddCreateForm, FreeAddCreateForm
import instaloader
import random
from django.contrib.auth.decorators import login_required

# Create your views here.
def win_view(request):
    context = {}
    form = AddCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # save the form data to model
        print('win_view')
        form.save()
        # print(form)
        
        # book_list = insta_model.objects.all()
        # print(book_list)

        # context= {'book_list':book_list}
        # print(context)

        a = insta_model.objects.values( 'insta_url', 'picker_kind', 'number_of_winers' )
        b = a[len(a)-1]
        user_insta_url_str = b["insta_url"]

        picker_kind = b["picker_kind"]
        number_of_winers = b["number_of_winers"]

        if number_of_winers == 0:
            number_of_winers = 1

        print(picker_kind)
        print(number_of_winers)

        PROFILE = "anis2423g"
        SHORTCODE = user_insta_url_str[28:39]
        print("Short code is: " + SHORTCODE)
               
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
            # print(comments_from_loop)
            
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

            # print(ran_like)
            the_winner_list = ran_like

        ### mentions
        elif picker_kind == 'mentions':
            comments_from_loop_owner = []
            comments_from_loop_text = []
            print("Fetching mentions of all posts of profile {}.".format(SHORTCODE))
            for post in profile.get_posts():
                post2 = post.from_shortcode(L.context, SHORTCODE)
                for x in post2.get_comments():
                    comments_from_loop_owner.append(x.owner)
                    comments_from_loop_text.append(x.text)
                
            a = []
            c = []
            for x in comments_from_loop_owner:
                a = str(x)
                b = a[9:-14]
                c.append(b)    

            comments_from_loop_owner = c

            mentioners_list =[]
            for i in comments_from_loop_text:
                aa = set(i)
                for j in aa:
                    if j == "@":
                        # print(i)
                        index = comments_from_loop_text.index(i)
                        # print(index)
                        mentioners_list.append(index)

            print(mentioners_list)
                
            mentioners_id = []
            for no in mentioners_list:
                bbb = comments_from_loop_owner[no]
                mentioners_id.append(bbb)

            # print(mentioners_id)

            the_winner_list = mentioners_id
        
        try:
            winner = random.sample(the_winner_list, int(number_of_winers))
            print("winner is {}".format(winner))

            context= {'winner':winner}
            print(context)

            return render(request, "about.html", context)
        
        except:
            winner = ['Something is Wrong with the Data!']
            context= {'winner':winner}
            print(context)

            return render(request, "about.html", context)
    else:
        print('else_win_view')
        # form.save()
        # print(form)
        
        # book_list = insta_model.objects.all()
        # print(book_list)

        # context= {'book_list':book_list}
        # print(context)

        a = insta_model.objects.values( 'insta_url', 'picker_kind', 'number_of_winers' )
        b = a[len(a)-1]
        user_insta_url_str = b["insta_url"]

        picker_kind = b["picker_kind"]
        number_of_winers = 1



        print(picker_kind)
        print(number_of_winers)

        PROFILE = "anis2423g"
        SHORTCODE = user_insta_url_str[28:39]
        print("Short code is: " + SHORTCODE)
               
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
            # print(comments_from_loop)
            
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

            # print(ran_like)
            the_winner_list = ran_like

        ### mentions
        elif picker_kind == 'mentions':
            comments_from_loop_owner = []
            comments_from_loop_text = []
            print("Fetching mentions of all posts of profile {}.".format(SHORTCODE))
            for post in profile.get_posts():
                post2 = post.from_shortcode(L.context, SHORTCODE)
                for x in post2.get_comments():
                    comments_from_loop_owner.append(x.owner)
                    comments_from_loop_text.append(x.text)
                
            a = []
            c = []
            for x in comments_from_loop_owner:
                a = str(x)
                b = a[9:-14]
                c.append(b)    

            comments_from_loop_owner = c

            mentioners_list =[]
            for i in comments_from_loop_text:
                aa = set(i)
                for j in aa:
                    if j == "@":
                        # print(i)
                        index = comments_from_loop_text.index(i)
                        # print(index)
                        mentioners_list.append(index)

            print(mentioners_list)
                
            mentioners_id = []
            for no in mentioners_list:
                bbb = comments_from_loop_owner[no]
                mentioners_id.append(bbb)

            # print(mentioners_id)

            the_winner_list = mentioners_id
        
        try:
            winner = random.sample(the_winner_list, int(number_of_winers))
            print("winner is {}".format(winner))

            context= {'winner':winner}
            print(context)

            return render(request, "about.html", context)
        
        except:
            winner = ['Something is Wrong with the Data!']
            context= {'winner':winner}
            print(context)

            return render(request, "about.html", context)

@login_required
def pick_view(request):
    context ={}
    print("pick_view")
    # create object of form
    form = AddCreateForm(request.POST or None, request.FILES or None)
      
    context['form']= form
    # print(context['form'])
    return render(request, "insta_app_templates/add.html", context)


def free_pick_view(request):
    context ={}
    print("free_pick_view")
    # create object of form
    form = FreeAddCreateForm(request.POST or None, request.FILES or None)
      
    context['form']= form
    # print(context['form'])
    return render(request, "insta_app_templates/add.html", context)