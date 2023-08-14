from django.contrib import admin
# import the post model from models.py
from .models import Post

# Register your models here.
# Register Post
admin.site.register(Post)
