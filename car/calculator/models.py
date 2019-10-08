from django.db import models

class ExchangeRate (models.Model):

    currency_code = models.CharField(max_length=20)

    date = models.DateField(max_length=20, help_text="Enter field documentation")

    exchange_rate = models.FloatField(max_length=20)

    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name
	
