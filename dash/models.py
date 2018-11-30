from django.db import models

# Create your models here.

class Underlying(models.Model):
	ticker = models.CharField(max_length=10)
	days_to_expiration = models.PositiveIntegerField()
	underlying_price = models.FloatField()
	delta = models.FloatField()


		