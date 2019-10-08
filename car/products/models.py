from django.db import models

# Create your models here.

class Car(models.Model):
    """Машина, которую выбирает покупатель"""
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=40)
    vin = models.CharField(max_length=17)
    year_of_prod = models.IntegerField(max_length=4)
    base_usd_price = models.IntegerField()

    def __str__(self):
        return self.make + " " + self.model + ", " + str(self.year_of_prod)


class Feature(models.Model):
    """Элемент комплектации, который добавляет покупатель к базовой комплектации автомобиля"""
    car = models.ForeignKey(Car,
          on_delete = models.CASCADE,
          null = True,
          blank = True,
          )
    feature_name = models.CharField(max_length=30)
    feature_usd_price = models.IntegerField()

    def __str__(self):
        return self.feature_name
        
