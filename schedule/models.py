from django.db import models
from teams.models import Team
# Create your models here.


class Schedule(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    date = models.DateField()
    time = models.TimeField()
    home = models.OneToOneField(
        Team, to_field='name', related_name='+', on_delete=models.PROTECT)
    away = models.OneToOneField(
        Team, to_field='name', related_name='+', on_delete=models.PROTECT)

    def __str__(self):
        return self.id
