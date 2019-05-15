from django.contrib import admin
from .models import Setting
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','status']
    # list_filter = ('name', 'price')

admin.site.register(Setting, SettingAdmin)