from rest_framework import serializers

from forum.models import ForumModel


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumModel
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at', 'status']
