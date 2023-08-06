from django_filters import rest_framework as filters

from notifications_plus import get_notification_model

NotificationModel = get_notification_model()


class NotificationFilter(filters.FilterSet):
    class Meta:
        model = NotificationModel
        fields = ["unread"]
