from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostUser(models.Model):
    user = models.ForeignKey(User, related_name='user_user', on_delete=models.CASCADE)
    subs = models.ForeignKey(User, related_name='subscribe_user', on_delete=models.CASCADE)