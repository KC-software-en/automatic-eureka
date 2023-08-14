# use get_object_or_404 in views.py to render a HTTP 404 error if a question with the requested ID doesn’t exist
from django.shortcuts import get_object_or_404, render
# import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# import the Question and Choice from models.py
from .models import Question, Choice
# Import the @login_required decorator
# ref: https://docs.djangoproject.com/en/4.2/topics/auth/default/
from django.contrib.auth.decorators import login_required
#############################################################################

# Create your views here.

# define index function referenced in polls/urls.py
# load the template called polls/poll.html and pass it a context.
# The context is a dictionary that maps template variable names to Python objects
# apply login decorator to each view a user may see only when logged in
# include optional login_url parameter to redirect user to login page
@login_required(login_url='user_auth:login')
def index(request):
    # comment out the HttpResponse to update code
    #return HttpResponse("Hello world. You're at the polls index.")
    # update our index view to render the poll.html template
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context is a dictionary that maps template variable names to Python objects
    context = {'latest_question_list': latest_question_list}
    # load the template called polls/poll.html and passes it a context
    return render(request, "polls/poll.html", context)

# write a view for the question to vote on, incl the argument question_id
# display the question text for a given poll
# render an HTTP 404 error if a question with the requested ID doesn’t exist
@login_required(login_url='user_auth:login')
def detail(request, question_id):
    # comment out HttpResponse
    # return HttpResponse(f"You're looking at question {question_id}")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# write a view for the results of the question, incl the argument question_id
@login_required(login_url='user_auth:login')
def results(request, question_id):
    # comment out HttpResponse
    # response = f"You're looking at the results of question {question_id}"
    # return HttpResponse(response)
    # from vote(), the redirected URL will then call the 'results' view to display the final page
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# write a view to vote on a question, incl the argument question_id
# it handles the submitted data
@login_required(login_url='user_auth:login')
def vote(request, question_id):
    # comment out HttpResponse
    # return HttpResponse(f"You're voting on question {question_id}")
    # pk refers to the primary key field of a database table
    # django automatically creates a primary key for each model
    question = get_object_or_404(Question, pk=question_id)
    # access submitted data by key name with a dictionary-like object- request.POST
    # use the key name choice which returns the ID of the selected choice
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
            )
    # raise a KeyError if the ID of the choice isn’t found
    # an error occurs if the mapping (dictionary) key was not located in the set of existing keys
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
            })
    else:
        # else add the vote and save the choice
        selected_choice.votes += 1
        selected_choice.save()
        # use HttpResponseRedirect instead of HttpResponse;
        # HttpResponseRedirect takes the URL to which the user will be redirected as an argument
        # Always return an HttpResponseRedirect after successfully
        # dealing with POST data. This prevents data from being
        # posted twice if a user hits the Back button.
        # use reverse function to take the name of the view and return the str value that represents the actual url
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
            )



