from django.urls import path
from .views import *

urlpatterns = [
    path('<int:userid>/', post_list, name="post_list_url"),
    path('<int:userid>/post/create', PostCreate.as_view(), name="post_create_url"),
    path('post/<str:slug>/', PostDetail.as_view(), name="post_detail_url"),
    path('<int:userid>/post/<str:slug>/readeble/', PostRead.as_view(), name="post_setreadeble_url"),
    path('<int:userid>/post/<str:slug>/update/', PostUpdate.as_view(), name="post_update_url"),
    path('<int:userid>/post/<str:slug>/delete/', PostDelete.as_view(), name="post_delete_url"),
]