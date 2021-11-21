import instaloader

L = instaloader.Instaloader()


PROFILE = "adighodsi_creation"

# Load session previously saved with `instaloader -l USERNAME`:
L.login("anis2423f", "anisanisanis") 
# USER = "anis2423f"
# L.load_session_from_file(USER, " ~\books\insta_app\session-anis2423f ")

profile = instaloader.Profile.from_username(L.context, PROFILE)

likes = []
print("Fetching likes of all posts of profile {}.".format(profile.username))
for post in profile.get_posts():
    print(post)
    likes = likes + list(post.get_likes())

print("Storing like into file.")
with open("inactive-users.txt", 'w') as f:
    for like in likes:
        print(like.username, file=f)


# for post in profile.get_posts():

    # post_likes = post.get_likes()
    # post_comments = post.get_comments()

    # print(post_likes)  # post_likes object
    # print(post_comments) # # post_comments object

    # post_likes.name  post_likes.username  post_likes.user    DOES NOT WORK
    # post_comments.name  post_comments.username  post_comments.user    DOES NOT WORK

    # Iterate over all likes of the post. A Profile instance of each likee is yielded.
    # for likee in post_likes:
    #     print(likee.username)

    # Iterate over all comments of the post.
    # Each comment is represented by a PostComment namedtuple with fields 
    # text (string), created_at (datetime), id (int), owner (Profile) 
    # and answers (~typing.Iterator[PostCommentAnswer]) if available.
    # for comment in post_comments:
        # print(comment.owner.username)




# likes = set()
# print("Fetching likes of all posts of profile {}.".format(profile.username))
# for post in profile.get_posts():
#     print(post)
#     likes = likes | set(post.get_likes())
    
# print(likes)

# print("Fetching followers of profile {}.".format(profile.username))
# followers = set(profile.get_followers())

# ghosts = followers - likes

# print("Storing ghosts into file.")
# with open("inactive-users.txt", 'w') as f:
#     for ghost in ghosts:
#         print(ghost.username, file=f)