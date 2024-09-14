from django.urls import path

from django.urls import include

from forum.api_views import forum_detail, forum_list

app_name = 'api_forum'

urlpatterns = [
    path('forum/', forum_list, name="forum"),
    path('forum/<int:pk>/', forum_detail, name="forumdetail"),
]
