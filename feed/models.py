from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

# Create your models here.

class PostUser(models.Model):
    user = models.ForeignKey(User, related_name='user_user', on_delete=models.CASCADE)
    subs = models.ForeignKey(User, related_name='subscribe_user', on_delete=models.CASCADE)

class PostRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)