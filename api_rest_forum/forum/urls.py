from django.urls import path

from django.urls import include
from rest_framework import routers

from forum.view_set import ForumViewSet


router = routers.DefaultRouter()
router.register(r'', ForumViewSet)

app_name = 'api_forum'

urlpatterns = [
    path('', include(router.urls)),
]