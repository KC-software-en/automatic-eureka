# import path for NameError: name 'path' is not defined
from django.urls import path, include
from . import views

# add an app_name to set the application namespace (multiple app project)
app_name = 'user_auth'

# create urls for views.py in user_auth app
# set a login path
# login.html references authenticate_user, so set up a path for it
# set a show user path
# set a path for user registration
# set a logout path
urlpatterns = [
    # comment out line below after checking it renders a page that says login
    # path('', views.index),    
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('show_user/', views.show_user, name='show_user'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('user_logout/', views.user_logout, name='logout')
    ]
