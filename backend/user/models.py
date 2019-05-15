import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from location.models import Country, Province, District

# Create your models here.
class Profile(AbstractUser):
    birthday = models.DateField(_('Birthday'), default=datetime.date.today)
    genderlist = (
        (1, 'Man'),
        (2, 'Woman'),
    )
    gender = models.IntegerField(_('Gender'), null=True, blank=True, choices=genderlist, default=1)
    profile = models.TextField(_('Profile'), null=True, blank=True)

    def __str__(self):
        return self.email

class Address(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    address1 = models.TextField(_('1st Address'), null=True, blank=True)
    address2 = models.TextField(_('2nd Address'), null=True, blank=True)
    county = models.CharField(_("County"), max_length=100, blank=True, null=True)
    city = models.CharField(_("City"), max_length=100, blank=True, null=True)
    postal_code = models.CharField(_("Postal Code"), max_length=100, blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=100, blank=True, null=True)
    mobile_phone = models.CharField(_("Mobile Phone"), max_length=100, blank=True, null=True)
    comment = models.TextField(_("Comment"), blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Addresses"

class Company(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    address1 = models.TextField(_('1st Address'), null=True, blank=True)
    address2 = models.TextField(_('2nd Address'), null=True, blank=True)
    county = models.CharField(_("County"), max_length=100, blank=True, null=True)
    city = models.CharField(_("City"), max_length=100, blank=True, null=True)
    tin = models.CharField(_("Tax Identification Number"), max_length=100, blank=True, null=True)
    trn = models.CharField(_("Trade Registry Number"), max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Companies"
