from django.contrib import admin

# Register your models here.

from products.models import Car, Feature

admin.site.register(Car)
admin.site.register(Feature)
