from rest_framework import serializers
from products.models import Car
from products.models import Feature
from django.contrib.auth.models import User


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feature
        fields = ('feature_name', 'feature_usd_price', 'car')

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('make', 'model', 'vin', 'year_of_prod', 'base_usd_price')


