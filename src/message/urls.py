from django.urls import path, include
from message.api_views import message_list




urlpatterns = [
     path('messages/',include([
            path('<int:subject_id>',message_list),
        ])),
]