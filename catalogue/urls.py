from django.urls import path, include
from . import views

# add an app_name to set the application namespace (multiple app project)
app_name = 'catalogue'

# set a path to the urls.py file referenced in the configuration directory urls.py of the django_website
# reference a function called index from views.py.
urlpatterns = [
    path('', views.index, name='index'),
    ]

