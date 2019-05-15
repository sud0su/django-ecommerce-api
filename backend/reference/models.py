from django.db import models
from django.utils.translation import gettext as _
from mptt.models import MPTTModel, TreeForeignKey
from decimal import Decimal
# Create your models here.

class Tax(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    value = models.DecimalField(_("Value"), max_digits=13, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "taxes"

class Currency(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    iso = models.CharField(_("ISO"), max_length=50, blank=True, null=True)
    value = models.DecimalField(_("Value"), max_digits=13, decimal_places=2, blank=True, null=True)
    default = models.IntegerField(_("Default"), default=0)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "currencies"

class Category(MPTTModel):
    name = models.CharField(_("Name"),max_length=50, unique=True)
    slug = models.SlugField(_("Slug"), max_length=100, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"
    class MPTTMeta:
        order_insertion_by = ['name']

class Notification(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    slug = models.SlugField(_("Slug"), max_length=100, blank=True, null=True)
    model = models.CharField(_("Model"), max_length=100, blank=True, null=True)
    body = models.TextField(_("Body"), blank=True, null=True)

    def __str__(self):
        return self.name

class Carrier(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    price = models.DecimalField(_("Price"), max_digits=13, decimal_places=2, blank=True, null=True)
    delivery_text = models.CharField(_("Delivery Text"), max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='carriers/logo', null=True, blank=True)

    def __str__(self):
        return self.name