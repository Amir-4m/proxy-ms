from django.db import models
from django.utils.translation import ugettext_lazy as _


class Proxy(models.Model):
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)
    host = models.CharField(_('host'), max_length=250)
    port = models.IntegerField(_('port'))
    username = models.CharField(_('username'), max_length=120, blank=True)
    password = models.CharField(_('password'), max_length=120, blank=True)
    is_enable = models.BooleanField(_('enabled?'))

    class Meta:
        verbose_name = _('Proxy')
        verbose_name_plural = _('Proxies')
        unique_together = ('host', 'port')

    def __str__(self):
        return f'{self.host}:{self.port}'
