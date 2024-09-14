from rest_framework import serializers
from .models import SujetModel



class SujetSerializer(serializers.ModelSerializer):

    class Meta:
        model = SujetModel
        fields = '__all__'