from django.db import models
from teams.models import Team
# Create your models here.


class Schedule(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    date = models.DateField()
    time = models.TimeField()
    home = models.ForeignKey(
        Team, to_field='name', related_name='home_matches', on_delete=models.CASCADE)
    away = models.ForeignKey(
        Team, to_field='name', related_name='away_matches', on_delete=models.CASCADE)
    game_data_saved = models.BooleanField(default=False)

    def __str__(self):
        return self.id


class GameData(models.Model):
    scheduled = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    lead_changes = models.IntegerField()
    teams_string = models.CharField(max_length=50, blank=False)
    home_points = models.IntegerField()
    away_points = models.IntegerField()
    home_scoring = models.JSONField()
    away_scoring = models.JSONField()
    OT = models.BooleanField(default=False)
    rating = models.DecimalField(decimal_places=1, max_digits=2, blank=True)

    def get_rating(self):
        self.rating = ((0.015 * (self.home_points + self.away_points)) - (0.01 * abs(
            self.home_points - self.away_points)) + (0.06 * self.lead_changes))
        if self.rating > 5:
            self.rating = 5
        self.save()

    def check_OT(self):
        if len(self.home_scoring) > 4:
            self.OT = True
        self.save()

    def __str__(self):
        return self.teams_string
