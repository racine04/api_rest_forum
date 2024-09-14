from django.urls import path

from django.urls import include
from rest_framework import routers

from message.view_set import MessageViewSet



router = routers.DefaultRouter()
router.register(r'', MessageViewSet)

app_name = 'api_message'

urlpatterns = [
    path('', include(router.urls)),
]