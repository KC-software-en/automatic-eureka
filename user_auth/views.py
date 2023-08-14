# import render and redirect(to send user to login after creation) from shortcuts
from django.shortcuts import render, redirect
# import to authenticate the user as well as django's login & logout functions
from django.contrib.auth import authenticate, login, logout
# import HttpResponseRedirect and reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# import django's default user creation form
# https://www.javatpoint.com/django-usercreationform
from django.contrib.auth.forms import UserCreationForm
# import the altered form
from .forms import AlterUserCreationForm
# import flash messages for successful new user creation
# - https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#using-messages-in-views-and-templates
from django.contrib import messages
#######################################################################################################

# Create your views here.
# define index function referenced in blog/urls.py
#def index(request):
 #   return HttpResponse("<h2>Login</h2>")


################delete above view!!!#################

# set up your user_login view in views.py to take the user to the login page
def user_login(request):
    return render(request, 'authentication/login.html')

# method to look up in the Users table and return an object that represents the logged-in user.
# if the user doesn’t exist in the table, simply return None.
# then send the user back to login if the object is None, and to a new welcome HTML page otherwise
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        messages.info(request, 'The username or password is incorrect.')
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:show_user'))

# read in the user data and send it to (and render) a new HTML file.
# In order to read the user data, this can simply be found in the request.user object:
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
        })

# register new user
def user_registration(request):
    # render the form
    # comment out default form and replace it with altered form
    # form = UserCreationForm()
    form = AlterUserCreationForm()

    # pass post data from html into the form
    if request.method == 'POST':
        # comment out default form and replace it with altered form
        # form = UserCreationForm(request.POST)
        form = AlterUserCreationForm(request.POST)
        # save the form if it is valid
        if form.is_valid():
            form.save()
            # add confirmation of new user creation
            # use a flash message that will display on the login.html page
            # include the user name in the message
            # - find all the validated form data in its cleaned_data attribute
            user = form.cleaned_data.get('username')
            messages.success(request, 'New account created for ' + user)

            # redirect new user to login page
            return redirect('user_auth:login')        
            
    # create a context dictionary that includes the form object
    # pass context to the render function along with the HTML template file name (user_registration.html)
    # The rendered HTML page is returned as the HTTP response.
    context ={'form': form}
    return render(request, 'authentication/user_registration.html', context)

# create a method to logout user & return user to login page
def user_logout(request):
    logout(request)
    return redirect('user_auth:login')        
