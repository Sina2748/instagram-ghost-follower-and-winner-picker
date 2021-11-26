import instaloader
import random


import xlwt
from django.http import HttpResponse


def download_excel_data(request):
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
	columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', ]

	#write column headers in sheet
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()

	#get your data, from database or from a text file...
	data = get_data() #dummy method to fetch data.
	for my_row in data:
		row_num = row_num + 1
		ws.write(row_num, 0, my_row.name, font_style)
		ws.write(row_num, 1, my_row.start_date_time, font_style)
		ws.write(row_num, 2, my_row.end_date_time, font_style)
		ws.write(row_num, 3, my_row.notes, font_style)

	wb.save(response)
	return response





# L = instaloader.Instaloader()

# url = "https://www.instagram.com/p/CM7mfVGAmYd/"
# url_ = url[28:39]

# print(url_)

# PROFILE = "anis2423g"
# SHORTCODE = "CWZzx09BZZ4"

# # Load session previously saved with `instaloader -l USERNAME`:
# # L.login("anis2423f", "anisanisanis") 
# USER = "anis2423g"
# L.load_session_from_file(USER)
# profile = instaloader.Profile.from_username(L.context, PROFILE)

# ff = profile.followers
# print(ff)

# likes = set()
# print("Fetching likes of all posts of profile {}.".format(profile.username))
# for post in profile.get_posts():
#     print(post)
#     likes = likes | set(post.get_likes())

# print("Fetching followers of profile {}.".format(profile.username))
# followers = set(profile.get_followers())

# ghosts = followers - likes

# print("Storing ghosts into file.")
# with open("inactive-users.txt", 'w') as f:
#     for ghost in ghosts:
#         print(ghost.username, file=f)






















# # comments_from_loop_owner = []
# # comments_from_loop_text = []
# # print("Fetching comments of all posts of profile {}.".format(SHORTCODE))
# # for post in profile.get_posts():
# #     post2 = post.from_shortcode(L.context, SHORTCODE)
# #     for x in post2.get_comments():
# #         comments_from_loop_owner.append(x.owner)
# #         comments_from_loop_text.append(x.text)
    
# # a = []
# # c = []
# # for x in comments_from_loop_owner:
# #     a = str(x)
# #     b = a[9:-14]
# #     c.append(b)    

# # comments_from_loop_owner = c

# # mentioners_list =[]
# # for i in comments_from_loop_text:
# #     aa = set(i)
# #     for j in aa:
# #         if j == "@":
# #             print(i)
# #             index = comments_from_loop_text.index(i)
# #             # print(index)
# #             mentioners_list.append(index)

# # print(mentioners_list)
    
# # mentioners_id = []
# # for no in mentioners_list:
# #     bbb = comments_from_loop_owner[no]
# #     mentioners_id.append(bbb)

# # print (mentioners_id)

# # winner = random.sample(mentioners_id, 1)
# # print("winners: {}".format(winner))

    


# # print("Storing like into file.")
# # with open("inactive-users.txt", 'w') as f:
# #     for like in likes:
# #         print(like.username, file=f)




# ### all the like of a profile
# # profile = instaloader.Profile.from_username(L.context, PROFILE)

# # likes = []
# # print("Fetching likes of all posts of profile {}.".format(profile.username))
# # for post in profile.get_posts():
# #     print(post)
# #     likes = likes + list(post.get_likes())

# # print("Storing like into file.")
# # with open("inactive-users.txt", 'w') as f:
# #     for like in likes:
# #         print(like.username, file=f)


# # for post in profile.get_posts():

#     # post_likes = post.get_likes()
#     # post_comments = post.get_comments()

#     # print(post_likes)  # post_likes object
#     # print(post_comments) # # post_comments object

#     # post_likes.name  post_likes.username  post_likes.user    DOES NOT WORK
#     # post_comments.name  post_comments.username  post_comments.user    DOES NOT WORK

#     # Iterate over all likes of the post. A Profile instance of each likee is yielded.
#     # for likee in post_likes:
#     #     print(likee.username)

#     # Iterate over all comments of the post.
#     # Each comment is represented by a PostComment namedtuple with fields 
#     # text (string), created_at (datetime), id (int), owner (Profile) 
#     # and answers (~typing.Iterator[PostCommentAnswer]) if available.
#     # for comment in post_comments:
#         # print(comment.owner.username)




# # likes = set()
# # print("Fetching likes of all posts of profile {}.".format(profile.username))
# # for post in profile.get_posts():
# #     print(post)
# #     likes = likes | set(post.get_likes())
    
# # print(likes)

# # print("Fetching followers of profile {}.".format(profile.username))
# # followers = set(profile.get_followers())

# # ghosts = followers - likes

# # print("Storing ghosts into file.")
# # with open("inactive-users.txt", 'w') as f:
# #     for ghost in ghosts:
# #         print(ghost.username, file=f)