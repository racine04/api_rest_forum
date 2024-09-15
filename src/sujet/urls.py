from django.urls import path, include
from rest_framework import routers
from .api_view import sujet_list, sujet_detail





urlpatterns = [
     path('subjects/<int:forum_id>/forum', sujet_list),
    path('subjects/<int:pk>/detail', sujet_detail),
]
