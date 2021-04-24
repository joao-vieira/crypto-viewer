from django.db import models

# Create your models here.
class Coin(models.Model):
	name 				= models.CharField(max_length = 120)
	short_name			= models.CharField(max_length = 5)
	price				= models.DecimalField(max_digits = 10, decimal_places = 2)
	market_cap			= models.DecimalField(max_digits = 20, decimal_places = 2)
	volume 				= models.DecimalField(max_digits = 20, decimal_places = 0)
	circulating_supply 	= models.DecimalField(max_digits = 20, decimal_places = 0)

