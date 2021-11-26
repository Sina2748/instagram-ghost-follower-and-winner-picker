from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Create your views here.
# books/views.py
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import insta_ghost_model, insta_model
from .forms import AddCreateForm, FreeAddCreateForm, AddCreateGhostForm
import instaloader
import random
from django.contrib.auth.decorators import login_required
import xlwt


# Create your views here.
# excel File
def download_excel_data_view(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')

	#decide file name
	response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

	#creating workbook
	wb = xlwt.Workbook(encoding='utf-8')

	#adding sheet
	ws = wb.add_sheet("sheet1")

	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	#column header names, you can use your own headers here
	columns = ['winners']

	#write column headers in sheet
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()

	#get your data, from database or from a text file...
	data = win_view.winner
	for my_row in data:
		row_num = row_num + 1
		ws.write(row_num, 0, my_row, font_style)


	wb.save(response)
	return response







# ghosts_are_view
def ghosts_are_view(request):
    win_view.winner = []
    context = {}
    form = AddCreateGhostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # save the form data to model
        print('ghosts_are_view')
        form.save()

        a = insta_ghost_model.objects.values( 'insta_ID' )
        b = a[len(a)-1]
        user_insta_ID_str = b["insta_ID"]
        print(user_insta_ID_str)
        

        PROFILE = user_insta_ID_str
        # SHORTCODE = user_insta_url_str[28:39]
        # print("Short code is: " + SHORTCODE)
               
        L = instaloader.Instaloader()

        # Load session previously saved with `instaloader -l USERNAME`:
        L.login("anis2423g", "anisanisanis") 
        # USER = "anis2423f"
        # L.load_session_from_file(USER)
        profile = instaloader.Profile.from_username(L.context, PROFILE)

        ff = profile.followers
        print(ff)

        if ff> 500:
            ghost_list = ["This account has more tha 500 followes. Currently it's not possible to find the ghost followers list"]
            context= {'winner':ghost_list}
            return render(request, "ghosts_are.html", context)




        likes = set()
        print("Fetching likes of all posts of profile {}.".format(profile.username))
        for post in profile.get_posts():
            print(post)
            likes = likes | set(post.get_likes())

        print("Fetching followers of profile {}.".format(profile.username))
        followers = set(profile.get_followers())

        ghosts = followers - likes
        ghost_list = []
        for ghost in ghosts:
            a = ghost.username
            ghost_list.append(a)

        print(ghost_list)
        win_view.winner = ghost_list
        # download_excel_data_view(data) = ghost_list
        context= {'winner':ghost_list}   

        # print("Storing ghosts into file.")
        # with open("inactive-users.txt", 'w') as f:
        #     for ghost in ghosts:
        #         print(ghost.username, file=f)

    return render(request, "ghosts_are.html", context)



# ghost_followers_view
def ghost_followers_view(request):

    context ={}
    print("ghost_followers_view")
    # create object of form
    form = AddCreateGhostForm(request.POST or None, request.FILES or None)
      
    context['form']= form
    # print(context['form'])
    return render(request, "ghost_followers.html", context)





# pick
def win_view(request):
    win_view.winner = []
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
            win_view.winner = winner
            print("winner is {}".format(winner))

            context= {'winner':winner}
            print(context)

            return render(request, "good_data.html", context)
        
        except:
            winner = ['Something is Wrong with the Data!']
            context= {'winner':winner}
            print(context)

            return render(request, "good_data.html", context)
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

            return render(request, "good_data.html", context)
        
        except:
            winner = ['Something is Wrong with the Data!']
            context= {'winner':winner}
            print(context)

            return render(request, "good_data.html", context)

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



