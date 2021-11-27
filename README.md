# instagram-ghost-follower-and-winner-picker
Here I use Django and Instaloader to build a website where users can pick winners or find their page ghost followers.
First, started a Django project and movied everything to a docker container. Added PostgreSQL and made the needed apps.
I also used Django Crispy Forms and Django-allauth, popular 3rd party package.
"Free picker" let's user try the service without singing up and paying, but only returns one winner.
"Winner picker" let's user find many winners from likes, comments and mentions of a post.
"Ghost follower" returns a list of all the followers of a page who have never liked a post.
All the lists are downloadable with a click of a button.
