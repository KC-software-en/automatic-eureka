from django.contrib import admin
# Register the Question class, so that it will be available when we login
# to the admin page of our site.

# import Question & Choice classes from models.py
from .models import Question
from .models import Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)

