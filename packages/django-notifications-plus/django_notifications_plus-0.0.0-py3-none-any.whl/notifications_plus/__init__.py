from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

VERSION = (0, 0, 1)
__version__ = ".".join(map(str, VERSION))


def get_notification_model():
    setting = getattr(
        settings,
        "NOTIFICATIONS_PLUS_NOTIFICATION_MODEL",
        "notifications_plus.Notification",
    )
    try:
        return django_apps.get_model(setting, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            "NOTIFICATIONS_PLUS_NOTIFICATION_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "NOTIFICATIONS_PLUS_NOTIFICATION_MODEL refers to model '%s' that has not been installed"
            % setting
        )
