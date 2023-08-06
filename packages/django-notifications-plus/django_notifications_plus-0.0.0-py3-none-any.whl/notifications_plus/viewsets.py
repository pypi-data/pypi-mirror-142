from django_filters import rest_framework as filters
from rest_framework import mixins, permissions
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from notifications_plus import get_notification_model
from notifications_plus.serializers import NotificationListSerializer

from .filters import NotificationFilter

NotificationModel = get_notification_model()


class NotificationViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filter_class = NotificationFilter
    serializer_class = NotificationListSerializer
    ordering = ["-created_at"]

    def get_queryset(self):
        user = self.request.user
        queryset = NotificationModel.objects.filter(recipient=user)
        return queryset
