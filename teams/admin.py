from django.contrib import admin
from .models import Team, Division, Conference
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    ordering = ("name",)


class ConferenceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'alias',
    )


class DivisionAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'alias',
    )


admin.site.register(Team, TeamAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Conference, ConferenceAdmin)
