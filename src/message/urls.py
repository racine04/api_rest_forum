from django.urls import path, include
from message.views import message_list



urlpatterns = [

     path('messages/',include([
            path('<int:sujet_id>/list',message_list),
        ])),

]