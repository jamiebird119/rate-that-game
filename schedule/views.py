from django.shortcuts import render
from .models import Schedule
from datetime import datetime


# Create your views here.


def schedule_search(request, date):
    template = 'schedule/schedule_search.html'
    search_date = datetime.strptime(date, "%Y-%m-%d")
    try:
        schedule = Schedule.objects.filter(date=search_date)
        games = []
        for item in schedule:
            try:
                game_data = schedule.game_data_set.get()
            except Exception as e:
                game_data = "Game Not Played. Please check back later"
            games.append({"schedule": item, "game_data": game_data})
        if not schedule:
            context = {
            'search_date': date,
            'date': datetime.strftime(search_date, '%A %d %B'),
            'message': 'There are currently no games on the selected date. Please check another.',
        }
        else:
            context = {
                'search_date': date,
                'date': datetime.strftime(search_date, '%A %d %B'),
                'games': games,
            }
    except Exception as e:
        print(e)
        context = {
            'search_date': date,
            'date': datetime.strftime(search_date, '%A %d %B'),
            'message': 'There are currently no games on the selected date. Please check another.',
        }
    return render(request, template, context)
