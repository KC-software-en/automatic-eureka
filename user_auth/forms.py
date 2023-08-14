# import django's default user creation form as done in views.py since there has to be a field added
# https://docs.djangoproject.com/en/4.2/topics/forms/#looping-over-the-form-s-fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
# import user from models- models viewed on admin page
from django.contrib.auth.models import User

# create a class that inherits from UserCreationForm
# - .: replicate form & customise it
class AlterUserCreationForm(UserCreationForm):
    # use meta class because it is the inner class in Django models
    # it contains meta options used to alter the behaviour of model fields
    class Meta:
        model = User
        # add the field for first name
        fields = ['username', 'password1', 'password2', 'first_name']
    
