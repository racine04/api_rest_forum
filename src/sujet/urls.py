from django.urls import path

from django.urls import include
from rest_framework import routers

from sujet.view_set import SujetViewSet


router = routers.DefaultRouter()
router.register(r'', SujetViewSet)

app_name = 'api_sujet'

urlpatterns = [
    path('', include(router.urls)),
]