from django.contrib import admin
from .models import Product, ProductImage, AttributeProductValue, SpesificPrice
# Register your models here.

class ProductImagesTabular(admin.TabularInline):
    model = ProductImage
    extra = 0
    min_num = 1

class AttributeProductValueTabular(admin.TabularInline):
    model = AttributeProductValue
    extra  = 0
    min_num = 1

class SpesificPriceTabular(admin.TabularInline):
    model = SpesificPrice
    extra  = 0
    min_num = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesTabular, AttributeProductValueTabular, SpesificPriceTabular]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)