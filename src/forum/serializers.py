from rest_framework import serializers

from forum.models import ForumModel

class ForumSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForumModel
        fields= ['title', 'description']