from django.db import models

# Create your models here.

class Car(models.Model):
    """Car being chosen by customer"""
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=40)
    vin = models.CharField(max_length=17)
    year_of_prod = models.IntegerField()
    base_usd_price = models.IntegerField()

    
    def __str__(self):
        return self.make + " " + self.model + ", " + str(self.year_of_prod)


class Feature(models.Model):
    """Equipment item being added to car base equipment by customer"""
    car = models.ForeignKey(Car,
          on_delete = models.CASCADE,
          null = True,
          blank = True,
          )
    feature_name = models.CharField(max_length=30)#FIXME: rename into value
    #TODO: add choise by type https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.Field.choices
    #TODO: add extra properties field https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/fields/#jsonfield
    feature_usd_price = models.IntegerField()

    def __str__(self):
        return self.feature_name
        
