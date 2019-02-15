from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from django_currentuser.middleware import get_current_user
from django.contrib.auth.models import User


# Create your models here.

def gen_slug(x):
    slug = slugify(x, allow_unicode=True)
    return slug+'-'+str(int(time()))

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.CharField(max_length=150, blank=True, unique=True)
    introtext = models.TextField(blank=True, db_index=True)
    fulltext = models.TextField(blank=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    readed = models.TextField(blank=True, db_index=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.user_id = get_current_user().id
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return self.title
