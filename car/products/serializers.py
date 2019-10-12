from rest_framework import serializers
from products.models import Car
from products.models import Feature
from django.contrib.auth.models import User



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('make', 'model', 'vin', 'year_of_prod', 'base_usd_price')


class FeatureSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    class Meta:
        model = Feature
        fields = ('feature_name', 'feature_usd_price', 'car')
