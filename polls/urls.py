from django.urls import path, include, re_path
from . import views

# add an app_name to set the application namespace (multiple app project)
# -  to ensure that Django knows which app view to create for a URL when using the {% url %} template tag
app_name = 'polls'

# set a path to the urls.py file referenced in the configuration directory urls.py of the django_website
# reference a function called index from views.py.
urlpatterns = [    
    path('', views.index, name='index'),
    # set a path for the question view
    path('<int:question_id>/', views.detail, name='detail'),
    # set a path for the results view
    path('<int:question_id>/results/', views.results, name='results'),
    # set a path for the vote view
    path('<int:question_id>/vote/', views.vote, name='vote')
    ]

