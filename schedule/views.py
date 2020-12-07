from django.shortcuts import render
from .models import Schedule
# Create your views here.


def schedule_search(request, date):
    template = 'schedule/schedule_search.html'
    games = Schedule.objects.all(date=date)
    context = {
        'date': date,
        'games': games,
    }
    return render(request, template, context)
