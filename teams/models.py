from django.db import models


# Create your models here.


class Team(models.Model):
    _id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=254, blank=False,
                            null=False, unique=True)
    alias = models.CharField(max_length=20, blank=False, null=False)
    ratings_home = models.JSONField(default=dict, blank=True)
    ratings_away = models.JSONField(default=dict, blank=True)
    home_rating = models.DecimalField(
        max_digits=3, blank=True, decimal_places=2, null=True)
    away_rating = models.DecimalField(
        max_digits=3, blank=True, decimal_places=2, null=True)
    image = models.ImageField(blank=True)

    def calc_rating(self):
        if self.ratings_home:
            sum = 0
            for value in self.ratings_home.keys():
                sum += self.ratings_home[value]
            self.home_rating = sum/len(self.ratings_home)
        if self.ratings_away:
            sum = 0
            for value in self.ratings_home.keys():
                sum += self.ratings_home[value]
            self.away_rating = sum/len(self.ratings_away)
        self.save()

    def __str__(self):
        return self.name
