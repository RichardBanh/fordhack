from rest_framework import serializers
from .models import MessageNotificationModel

class MessageNotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageNotificationModel
        fields = (
            'uuid',
            'vehicleId',
            'last_sent',
            'messageType',
            'text',
            'web',
            'message',
            'active_Rental',
            'text_sent'
        )