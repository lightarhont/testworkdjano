from django.contrib import admin
from .models import Post
from .utils import mailsend 


class AuthorAdmin(admin.ModelAdmin):
    
    fields = ['title', 'slug', 'introtext', 'fulltext']
    
    def save_model(self, request, obj, form, change):
        obj.save()
        mailsend(request, obj.slug)

admin.site.register(Post, AuthorAdmin)