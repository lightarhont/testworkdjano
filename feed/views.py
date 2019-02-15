from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import Post
from .models import PostUser
from django.urls import reverse

# Create your views here.

def feed_list(request):
    posts = Post.objects.all()
    return render(request, 'feed/index.html', context={'posts': posts})

def feed_fav_list(request):
    pu = PostUser.objects.filter(user_id=request.user.id).all()
    l=[]
    for i in pu:
        l.append(i.subs_id)
    posts = Post.objects.filter(user_id__in=l)
    return render(request, 'feed/index.html', context={'posts': posts})

def subscribeuser(request, userid):
    pu = PostUser.objects.filter(subs_id=userid).filter(user_id=request.user.id).count()
    return render(request, 'feed/userblog.html', context={
        'posts': Post.objects.filter(user_id=userid),
        'user_id': userid,
        'subsribestatus': pu})

def subscribelist(request):
    posts = Post.objects.all()
    return render(request, 'feed/index.html', context={'posts': posts})

class ToSubscribe(View):
    def post(self, request, userid):
        pu = PostUser(subs_id=userid, user_id=request.user.id)
        pu.save()
        return redirect(reverse('feed_list_url'))

class UnSubscribe(View):
    def post(self, request, userid):
        pu = PostUser.objects.filter(subs_id=userid).filter(user_id=request.user.id)
        pu.delete()
        return redirect(reverse('feed_list_url'))