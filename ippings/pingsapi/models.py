from django.db import models

# Create your models here.

class Location(models.Model):
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)

class Country(models.Model):
    country_name = models.CharField(blank=True, max_length=60)
    country_code = models.CharField(blank=True, max_length=10)

class Ping(models.Model):
    country = models.ForeignKey(Country, null=True ,on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    time = models.DateField(blank=False)
    ip_addr = models.GenericIPAddressField()