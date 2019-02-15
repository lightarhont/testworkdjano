from django.contrib import admin
from .models import Post


class AuthorAdmin(admin.ModelAdmin):
    
    fields = ['title', 'slug', 'introtext', 'fulltext']


admin.site.register(Post, AuthorAdmin)