from django.urls import path, include
from rest_framework import routers
from .viewset import SujetViewset
from .api_view import sujet_list, sujet_detail


app_name = 'api_sujet'

router = routers.DefaultRouter()
router.register(r'sujets', SujetViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('subjects/', sujet_list),
    path('subjects/<int:pk>/', sujet_detail),
]
