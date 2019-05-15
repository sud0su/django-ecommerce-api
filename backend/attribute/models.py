from django.db import models
from django.contrib import admin
from django.utils.translation import gettext as _

# Create your models here.
class Attribute(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    listtype = (
        ('text','Text'),
        ('textarea','Text Area'),
        ('date', 'Date'),
        ('multiple_select', 'Multiple Select'),
        ('dropdown', 'Dropdown'),
        ('media', 'Media'),
    )
    type = models.CharField(_("Type"), max_length=50, blank=True, null=True, choices=listtype)
    def __str__(self):
        return self.name

class AttributeSet(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class AttributeValue(models.Model):
    value = models.CharField(_("Value"), max_length=100, blank=True, null=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.value

class AttributeAttributeSet(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)
    attributeset = models.ForeignKey(AttributeSet, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)