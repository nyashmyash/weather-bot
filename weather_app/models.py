from django.db import models


class City(models.Model):
    name = models.TextField(default='')
    lon = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    lat = models.DecimalField(max_digits=10, decimal_places=5, default=0)
