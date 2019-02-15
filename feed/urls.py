from django.urls import path
from .views import *

urlpatterns = [
    path('', feed_list, name="feed_list_url"),
    path('favorites/', FeedFavList.as_view(), name="feed_favorites_list_url"),
    path('<int:userid>/subscribeopt/', SubscribeUser.as_view(), name="subscribe_user_url"),
    path('<int:userid>/tosubscribe/', ToSubscribe.as_view(), name="tosubscribe_user_url"),
    path('<int:userid>/unsubscribe/', UnSubscribe.as_view(), name="unsubscribe_user_url"),
]