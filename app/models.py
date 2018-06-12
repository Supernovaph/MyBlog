from django.db import models

# Post
# Comment
# User
class BlogUser(models.Model):
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class Post(models.Model):
    author = models.ForeignKey(BlogUser, on_delete=models.DO_NOTHING)
    created = models.DateTimeField()
    title = models.CharField(max_length=255)
    text = models.TextField()
