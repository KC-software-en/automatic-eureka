# specify the resource to return when a certain HTTP request is made using a specific URL
from django.urls import path, include
from . import views
#
from .models import Post
# import Django’s generic class-based view classes: ListView, to present a list on the webpage to the user.
# import the generic DetailView so that individual blog posts have their own page
from django.views.generic import ListView, DetailView

# add an app_name to set the application namespace (multiple app project)
app_name = 'blog'

# set a path to the urls.py file referenced in the configuration directory urls.py of the django_website
# reference a function called index from views.py.
# comment out index below after confirming pg works
# urlpatterns = [
#   path('', views.index),
#  ]
# add a name for the blog because it's href in the navbar in header.html
urlpatterns = [
    # access the data stored about posts by referencing the model, Post.
    # list the last 25 blog posts ordered by date, in descending order with - (minus) sign
    path('',
        ListView.as_view(
            queryset=
            Post.objects.all().order_by("-date")[:25],
            template_name="blog.html",            
            ), name = "blog home"
        ),
    # access the data stored about posts by referencing the model, Post.
    # connect a specific blog entry in the database and display the information
    # - Each blog post object will be stored in a row in a database table
    # - Django identifies each entry by its primary key (pk)
    path('<int:pk>/',
        DetailView.as_view(
            model = Post,
            template_name="post.html"
            )
        ),
]
