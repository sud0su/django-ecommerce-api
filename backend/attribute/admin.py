from django.contrib import admin
from .models import Attribute, AttributeSet, AttributeValue, AttributeAttributeSet

# Register your models here.
class AttributeValueTabularInline(admin.TabularInline):
    model = AttributeValue
    extra = 0
    min_num = 1

class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name','type',)
    inlines = [AttributeValueTabularInline]

    class Meta:
        model = Attribute

admin.site.register(Attribute, AttributeAdmin)

class AttributeAttributeSetTabularInline(admin.TabularInline):
    model = AttributeAttributeSet
    extra = 0
    min_num = 1

class AttributeSetAdmin(admin.ModelAdmin):
    inlines = [AttributeAttributeSetTabularInline]
    list_display = ('name',)

    class Meta:
        model = AttributeSet

admin.site.register(AttributeSet, AttributeSetAdmin)

# change admin template
# change_list_template = 'admin/attribute/attribute_change_list.html'
# change_form_template = 'admin/attribute/attribute_change_form.html'