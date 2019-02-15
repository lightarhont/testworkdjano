from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import Post
from .models import PostUser, PostRead
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def feed_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'feed/index.html', context={'posts': posts})

class FeedFavList(View, LoginRequiredMixin):
    raise_exception = True
    def get(self, request):
        pu = PostUser.objects.filter(user_id=request.user.id).all().order_by('-id')
        l=[]
        for i in pu:
            l.append(i.subs_id)
        pr = PostRead.objects.filter(user_id=request.user.id)
        l2=[]
        for i in pr:
            l2.append(i.post_id)
        posts = Post.objects.filter(user_id__in=l).exclude(id__in=l2)
        return render(request, 'feed/index.html', context={'posts': posts})

class SubscribeUser(View, LoginRequiredMixin):
    raise_exception = True
    def get(self, request, userid):
        pu = PostUser.objects.filter(subs_id=userid).filter(user_id=request.user.id).count()
        return render(request, 'feed/userblog.html', context={
            'posts': Post.objects.filter(user_id=userid),
            'user_id': userid,
            'subsribestatus': pu})

class ToSubscribe(View):
    def post(self, request, userid):
        pu = PostUser(subs_id=userid, user_id=request.user.id)
        pu.save()
        return redirect(reverse('feed_list_url'))

class UnSubscribe(View):
    def post(self, request, userid):
        pu = PostUser.objects.filter(subs_id=userid).filter(user_id=request.user.id)
        pu.delete()
        pr = PostRead.objects.filter(user_id=request.user.id).all()
        pr.delete()
        return redirect(reverse('feed_list_url'))