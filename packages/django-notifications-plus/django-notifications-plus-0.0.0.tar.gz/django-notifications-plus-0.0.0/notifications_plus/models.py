from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class AbstractNotification(models.Model):
    content = models.TextField(_("content"))
    unread = models.BooleanField(_("unread"), default=True)
    created_at = models.DateTimeField(_("created at"), default=None)
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("recipient"),
        related_name="notifications",
        on_delete=models.CASCADE,
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("actor"),
        related_name="+",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    action_object_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    action_object_object_id = models.CharField(max_length=255, blank=True, null=True)
    action_object = GenericForeignKey(
        "action_object_content_type", "action_object_object_id"
    )

    class Meta:
        abstract = True
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")

    def __str__(self):
        return "%s's notification: %s..." % (self.recipient, self.content[:50])

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        super().save(*args, **kwargs)


class Notification(AbstractNotification):
    class Meta(AbstractNotification.Meta):
        swappable = "NOTIFICATIONS_PLUS_NOTIFICATION_MODEL"
