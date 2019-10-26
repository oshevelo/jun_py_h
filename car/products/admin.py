from django.contrib import admin
from products.models import Car, Feature

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 3


class CarAdmin(admin.ModelAdmin):
    fieldsets = [(None,               {'fields': ['make', 'model', 'vin', 'year_of_prod',        'base_usd_price']})]
    inlines = [FeatureInline]
    list_display = ['make', 'model', 'vin', 'year_of_prod',        'base_usd_price']
    search_fields = ['make', 'model', 'vin', 'year_of_prod',        'base_usd_price']


admin.site.register(Car, CarAdmin)
admin.site.register(Feature)
