from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from decimal import Decimal
from reference.models import Currency, Carrier
from product.models import Product

class OrderStatus(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    notification = models.IntegerField(_("Notifications"), default=1)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "order statuses"

class Order(models.Model):
    shipping_address_id = models.IntegerField(_("Shipping Address ID"), null=True, blank= True)
    billing_address_id = models.IntegerField(_("Billing Address ID"), null=True, blank= True)
    billing_company_id = models.IntegerField(_("Billing Company ID"), null=True, blank= True)
    comment = models.CharField(_("Comment"), max_length=100, blank=True, null=True)
    shipping_no = models.CharField(_("Shipping No"), max_length=100, blank=True, null=True)
    invoice_no = models.CharField(_("Invoice No"), max_length=100, blank=True, null=True)
    invoice_date = models.DateTimeField(_("Invoice Date"))
    delivery_date = models.DateTimeField(_("Delivery Date"))
    total_discount = models.DecimalField(_("Total Discount"), max_digits=13, decimal_places=2, blank=True)
    total_discount_tax = models.DecimalField(_("Total Discount Tax"), max_digits=13, decimal_places=2, blank=True)
    total_shipping = models.DecimalField(_("Total Shipping"), max_digits=13, decimal_places=2, blank=True)
    total_shipping_tax = models.DecimalField(_("Total Shipping Tax"), max_digits=13, decimal_places=2, blank=True)
    total = models.DecimalField(_("Total"), max_digits=13, decimal_places=2, blank=True)
    total_tax = models.DecimalField(_("Total Tax"), max_digits=13, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.DO_NOTHING)
    carrier = models.ForeignKey(Carrier, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.comment


class OrderHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(OrderStatus, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "order histories"

class OrderProduct(models.Model):
    name = models.CharField(_("Name"), max_length=255, blank=True, null=True)
    sku = models.CharField(_("SKU"), max_length=100, blank=True, null=True)
    price = models.DecimalField(_("Price"), max_digits=13, decimal_places=2, blank=True, null=True)
    price_with_tax = models.DecimalField(_("Price with Tax"), max_digits=13, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(_("Quantity"))

    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name