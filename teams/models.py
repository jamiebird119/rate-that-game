from django.db import models
from colorfield.fields import ColorField


# Create your models here.
class Conference(models.Model):
    name = models.CharField(max_length=26, blank=False)
    alias = models.CharField(max_length=26, blank=False, default="")
    id = models.CharField(max_length=50, blank=False, primary_key=True)

    def __str__(self):
        return self.name


class Division(models.Model):
    name = models.CharField(max_length=35, blank=False)
    id = models.CharField(max_length=50, blank=False, primary_key=True)
    alias = models.CharField(max_length=26, blank=False, default="")
    conference = models.ForeignKey(
        Conference, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=254, blank=False,
                            null=False, unique=True)
    alias = models.CharField(max_length=20, blank=False, null=False)
    ratings_home = models.JSONField(default=dict, blank=True)
    team_color = ColorField(default="#FF0000")
    text_color = ColorField(default="#FFFFFF")
    ratings_away = models.JSONField(default=dict, blank=True)
    home_rating = models.DecimalField(
        max_digits=3, blank=True, decimal_places=2, null=True)
    away_rating = models.DecimalField(
        max_digits=3, blank=True, decimal_places=2, null=True)
    avg_rating = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True)
    image = models.ImageField(blank=True)
    conference = models.ForeignKey(
        Conference, on_delete=models.SET_NULL, null=True, blank=True)
    division = models.ForeignKey(
        Division, on_delete=models.SET_NULL, null=True, blank=True)
    wins = models.IntegerField(default=0, blank=True)
    loses = models.IntegerField(default=0, blank=True)
    win_pct = models.DecimalField(
        decimal_places=2, max_digits=4, default=0, blank=True)
    div_rank = models.IntegerField(default=0)
    conf_rank = models.IntegerField(default=0)

    def calc_average(self):
        if self.home_rating is not None and self.away_rating is not None:
            self.avg_rating = ((self.home_rating + self.away_rating)/2)
        elif self.home_rating is None:
            self.avg_rating = self.away_rating
        elif self.away_rating is None:
            self.avg_rating = self.home_rating
        else:
            self.avg_rating = 0
        self.save()

    def calc_rating(self):
        if self.ratings_home:
            sum = 0
            for value in self.ratings_home.keys():
                sum += self.ratings_home[value]
            self.home_rating = sum/len(self.ratings_home)
        if self.ratings_away:
            sum = 0
            for value in self.ratings_away.keys():
                sum += self.ratings_away[value]
            self.away_rating = sum/len(self.ratings_away)
        self.calc_average()
        self.save()

    def __str__(self):
        return self.name
