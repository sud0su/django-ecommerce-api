from django.contrib import admin
import nested_admin
from django.utils.html import format_html
from django.utils.translation import gettext as _
from mptt.admin import DraggableMPTTAdmin
from .models import Tax, Category, Notification, Currency, Carrier

# Register your models here.
class CategoriesAdmin(DraggableMPTTAdmin):
    fields = ('name','slug')
    list_display = ('tree_actions', 'getname','slug')
    list_display_links = ('getname',)
    prepopulated_fields = {'slug': ('name',)}

    def getname(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,  # Or whatever you want to put here
        )
    getname.short_description = _('Name')

class CarriersAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','delivery_text']
    # list_filter = ('name', 'price')

admin.site.register(Carrier, CarriersAdmin)
admin.site.register(Category, CategoriesAdmin)
admin.site.register([Tax, Notification, Currency])