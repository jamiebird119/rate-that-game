from django.db import models

# Create your models here.


class Team(models.Model):
    _id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=254, blank=False,
                            null=False, unique=True)
    alias = models.CharField(max_length=20, blank=False, null=False)
    ratings_home = models.JSONField(blank=True, default=list)
    ratings_away = models.JSONField(blank=True, default=list)
    home_rating = models.DecimalField(
        max_digits=3, blank=True, decimal_places=2, null=True)
    away_rating = models.DecimalField(
        max_digits=3, blank=True, decimal_places=2, null=True)
    image = models.ImageField(blank=True)

    def add_away_rating(self, id, rating):
        self.ratings_away += {id: rating}
        self.calc_rating()
        self.save()

    def add_home_rating(self, id, rating):
        self.ratings_home += {id: rating}
        self.calc_rating()
        self.save()

    def calc_rating(self):
        if self.ratings_home:
            self.home_rating = sum(self.ratings_home)/len(self.ratings_home)
        if self.ratings_away:
            self.away_rating = sum(self.ratings_away)/len(self.ratings_away)
        self.save()

    def __str__(self):
        return self.name
