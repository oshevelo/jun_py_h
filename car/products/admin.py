from django.contrib import admin
from products.models import Car, Feature

class FeatureInline(admin.StackedInline):
    model = Feature
    extra = 3


class CarAdmin(admin.ModelAdmin):
    fieldsets = [(None,               {'fields': ['make', 'model', 'vin', 'year_of_prod',        'base_usd_price']})]
    inlines = [FeatureInline]



admin.site.register(Car, CarAdmin)
admin.site.register(Feature)
