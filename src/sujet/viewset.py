from rest_framework import viewsets
from .models import SujetModel
from .serializers import SujetSerializer


class SujetViewset(viewsets.ModelViewSet):
    queryset = SujetModel.objects.all()
    serializer_class = SujetSerializer