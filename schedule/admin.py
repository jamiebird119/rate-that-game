from django.contrib import admin
from .models import Schedule

# Register your models here.


class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'time', 'home', 'away',
    )
    ordering = ('date',)


admin.site.register(Schedule, ScheduleAdmin)
