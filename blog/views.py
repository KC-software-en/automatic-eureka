from django.shortcuts import render
# import HttpResponse
from django.http import HttpResponse
# import Django’s generic class-based view classes: ListView, to present a list on the webpage to the user.
# import the generic DetailView so that individual blog posts have their own page
# resource codemy
from django.views.generic import ListView, DetailView
# import Post from models.py
from .models import Post
# Import the @login_required decorator
# ref: https://docs.djangoproject.com/en/4.2/topics/auth/default/
from django.contrib.auth.decorators import login_required
#############################################################################

# Create your views here.
# define index function referenced in blog/urls.py
# comment out index below after confirming pg works
#def index(request):
#    return HttpResponse("<h2>Blog</h2>")

# view for list of blog posts
# apply login decorator to each view a user may see only when logged in
# include optional login_url parameter to redirect user to login page
@login_required(login_url='user_auth:login')
def post_list(ListView):
    model = Post
    template = 'blog.html'
    return render(ListView, template)

# view for individual blog posts
@login_required(login_url='user_auth:login') 
def post_detail(DetailView):
    model = Post
    template = 'post.html'
    return render(DetailView, template)
