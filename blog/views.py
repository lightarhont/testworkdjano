from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import *
from feed.models import PostRead as PR

# Create your views here.

def post_list(request, userid):
    return render(request, 'blog/index.html', context={'posts': Post.objects.filter(user_id=userid)})

class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        if request.user.id:
            pr = PR.objects.filter(post_id=post.id).filter(user_id=request.user.id).count()
            if pr != 0:
                readed=True
            else:
                readed=False
        else:
            readed=True
        return render(request, 'blog/detail.html', context={'post': post, 'readed': readed})

class PostCreate(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request, userid):
        form = PostForm
        return render(request, 'blog/post_create.html', context={'form': form})
    def post(self, request, userid):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            mailsend(request, new_post.slug)
            return redirect(new_post)
        return render(request,'blog/post_create.html', context={'form':bound_form})

class PostUpdate(OwnerRequiredMixin, View):
    raise_exception = True
    def get(self, request, slug, userid):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(instance=post)
        return render(request, 'blog/post_update.html', context={'form': bound_form, 'post': post})
    
    def post(self, request, slug, userid):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=post)
        
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'blog/post_update.html', context={'form': bound_form, 'post': post})

class PostDelete(OwnerRequiredMixin, View):
    raise_exception = True
    def get(self, request, slug, userid):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_delete.html', context={'post': post})
    
    def post(self, request, slug, userid):
        post = Post.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('post_list_url', kwargs={'userid': request.user.id}))

class PostRead(View):
    def post(self, request, slug, userid):
        post = Post.objects.get(slug__iexact=slug)
        pr = PR(post_id=post.id, user_id=userid)
        pr.save()
        return redirect(reverse('feed_list_url'))
    