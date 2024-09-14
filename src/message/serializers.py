from rest_framework import serializers
from message.models import MessageModel


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageModel
        fields = ['name', 'post', 'created_at', 'updated_at', 'status']
        read_only_fields = ['created_at', 'updated_at', 'status']