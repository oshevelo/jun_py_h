from django.shortcuts import render
from rest_framework import viewsets
from products.models import Car, Feature
from products.serializers import CarSerializer, FeatureSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('-make')
    serializer_class = CarSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

