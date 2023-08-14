from django.db import models

# Create your models here.
# each model generally maps to a single database table.
# Models contain metadata about your application's data.
# A database is a repository data storage that your app needs access to over a long period
# Each class in models.py is a database table
class Post(models.Model):
    # Default behaviour - Django creates primary keys for you
    # Manually setting the primary key (optional): id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 140)
    body = models.TextField()
    # add a new field called signature
    # In addition to max_length, add a new parameter called default and set this to whatever you like
    # (your name, favourite quote etc.). This should be a string.
    signature = models.CharField(max_length = 140, default = "It is tender and delicious")
    date = models.DateTimeField()
    

    def __str__(self):
        return self.title
