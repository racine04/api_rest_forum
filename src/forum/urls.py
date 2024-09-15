from django.urls import path

from django.urls import include

from forum.api_views import forum_detail, forum_list


urlpatterns = [
    path('forums/', forum_list),
    path('forums/<int:pk>/', forum_detail),
]
