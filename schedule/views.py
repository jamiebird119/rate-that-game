from django.shortcuts import render
from .models import Schedule
from datetime import datetime


# Create your views here.


def schedule_search(request, date):
    template = 'schedule/schedule_search.html'
    search_date = datetime.strptime(date, "%Y-%m-%d")
    try:
        games = Schedule.objects.filter(date=search_date)
        if not games:
            context = {
            'date': datetime.strftime(search_date, '%A %d %B'),
            'message': 'There are currently no games on the selected date. Please check another.',
        }
        else:
            context = {
                'date': datetime.strftime(search_date, '%A %d %B'),
                'games': games,
            }
    except Exception as e:
        print(e)
        context = {
            'date': datetime.strftime(search_date, '%A %d %B'),
            'message': 'There are currently no games on the selected date. Please check another.',
        }
    return render(request, template, context)
