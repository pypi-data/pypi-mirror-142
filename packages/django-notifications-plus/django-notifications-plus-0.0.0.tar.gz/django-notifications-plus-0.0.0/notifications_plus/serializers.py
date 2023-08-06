from rest_framework import serializers

from notifications_plus import get_notification_model

NotificationModel = get_notification_model()


class NotificationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = [
            "content",
            "unread",
            "created_at",
            "recipient",
        ]
