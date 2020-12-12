from django.contrib import admin
from .models import Schedule, GameData

# Register your models here.


class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'time', 'home', 'away',
    )
    ordering = ('date',)


class GameDataAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'teams_string', 'rating', 'OT'
    )


admin.site.register(GameData, GameDataAdmin)
admin.site.register(Schedule, ScheduleAdmin)
