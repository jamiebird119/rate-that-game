from django.db import models

# Create your models here.


class Team(models.Model):
    _id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=254, blank=False, null=False, unique=True)
    alias = models.CharField(max_length=20, blank=False, null=False)
    home_rating = models.DecimalField(
        max_digits=3, blank=True, decimal_places=2, null=True)
    away_rating = models.DecimalField(
        max_digits=3, blank=True, decimal_places=2, null=True)
    image = models.ImageField()

    def __str__(self):
        return self.name
