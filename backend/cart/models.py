from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from decimal import Decimal
from product.models import Product, ProductGroup
from reference.models import Currency, Category

# Create your models here.
class CartRule(models.Model):
    name = models.CharField(_("Name"), max_length=250, blank=True, null=True)
    code = models.CharField(_("Code"), max_length=100, blank=True, null=True)
    priority = models.IntegerField(_("Priority"), blank=True, null=True)
    start_date = models.DateTimeField(_("Start Date"), auto_now=True, editable=True)
    expiration_date = models.DateTimeField(_("Expiration Date"))
    status = models.BooleanField(_("Status"),default=0)
    highlight = models.BooleanField(_("Highlight"),default=0)
    minimum_amount = models.IntegerField(_("Minimum Amount"), default=0)
    free_delivery = models.BooleanField(_("Free Delivery"),default=0)
    total_available = models.IntegerField(_("Total Available"), blank=True, null=True)
    total_available_each_user = models.IntegerField(_("Total Available Each User"), blank=True, null=True)
    promo_label = models.CharField(_("Promo Label"), max_length=250, blank=True, null=True)
    promo_text = models.TextField(_("Promo Text"), blank=True, null=True)
    multiply_gift = models.IntegerField(_("Multiply Gift"), default=1)
    min_nr_products = models.IntegerField(_("Min Nr Products"), default=0)
    TYPE_OF_DISCOUNT = (
        (0, 'Percent - order'),
        (1, 'Percent - selected products'),
        (2, 'Percent - cheapest product'),
        (3, 'Percent - most expensive product'),
        (4, 'Amount - order')
    )
    discount_type = models.CharField(_("Discount Type"),choices=TYPE_OF_DISCOUNT, max_length=1, default=0)
    reduction_amount = models.DecimalField(_("Reduction Amount"), max_digits=13, decimal_places=2, default=Decimal('0'))

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    gift_product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    reduction_currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, related_name="reduction_currency")
    minimum_ammount_currency_id = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, related_name="minimum_ammount_currency_id")

    def __str__(self):
        return self.name

class CartRulesCustomer(models.Model):
    cart_rule = models.ForeignKey(CartRule, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartRulesCategory(models.Model):
    cart_rule = models.ForeignKey(CartRule, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartRulesProduct(models.Model):
    cart_rule = models.ForeignKey(CartRule, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartRulesProductsGroup(models.Model):
    cart_rule = models.ForeignKey(CartRule, on_delete=models.DO_NOTHING)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartRulesCombination(models.Model):
    cart_rule_id1 = models.ForeignKey(CartRule, on_delete=models.DO_NOTHING, related_name="cart_rule_id1")
    cart_rule_id2 = models.ForeignKey(CartRule, on_delete=models.DO_NOTHING, related_name="cart_rule_id2")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
