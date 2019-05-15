from django.db import models
from django.utils.translation import gettext as _
from mptt.models import MPTTModel, TreeForeignKey
from decimal import Decimal
# Create your models here.

class Country(models.Model):
    code = models.CharField(_("Country Code"), max_length=50, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "countries"

class Province(models.Model):
    code = models.CharField(_("Province Code"), max_length=50, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class District(models.Model):
    code = models.CharField(_("District Code"), max_length=50, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
