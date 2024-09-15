from django.urls import path
from .api_view import sujet_list, sujet_detail


app_name = 'api_sujet'

urlpatterns = [
    path('subject/<int:forum_id>/forum', sujet_list),
    path('subject/<int:pk>/detail', sujet_detail),
]
