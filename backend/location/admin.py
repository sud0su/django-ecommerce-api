from django.contrib import admin
import nested_admin
from .models import Country, Province, District

# Register your models here.
class DistrictTabular(nested_admin.NestedTabularInline):
    model = District
    extra = 0
    min_num = 1

class ProvincesTabular(nested_admin.NestedTabularInline):
    model = Province
    extra = 0
    min_num = 1
    inlines = [DistrictTabular]

class CountriesAdmin(nested_admin.NestedModelAdmin):
    inlines = [ProvincesTabular]
    search_fields = ('name',)

class DistrictTab(admin.TabularInline):
    model = District
    extra = 0
    min_num = 1

class ProvincesAdmin(admin.ModelAdmin):
    inlines = [DistrictTab]
    search_fields = ('name',)

admin.site.register(Province, ProvincesAdmin)
admin.site.register(Country, CountriesAdmin)
admin.site.register([District])