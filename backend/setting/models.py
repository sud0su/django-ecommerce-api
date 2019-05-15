from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Setting(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    key = models.CharField(_("Key"), max_length=100, blank=True, null=True)
    value = models.TextField(_("Settings Values"), blank=True, null=True)
    field = models.TextField(_("Fields"), blank=True, null=True)
    status = (
        (0, 'No Active'),
        (1, 'Active')
    )
    active = models.IntegerField(_('Status Active'), null=True, blank=True, choices=status, default=0)

    def __str__(self):
        return self.name
