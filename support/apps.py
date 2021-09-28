from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SupportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'support'
    verbose_name = _('support')


