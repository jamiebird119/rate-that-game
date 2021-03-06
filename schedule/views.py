from django.shortcuts import render
from .models import Schedule, GameData
from datetime import datetime, timedelta


# Create your views here.


def schedule_search(request, date):
    template = 'schedule/schedule_search.html'
    if date == 'today':
        search_date = datetime.today()
        print(search_date)
    else:
        search_date = datetime.strptime(date, "%Y-%m-%d")
    prev = search_date - timedelta(days=1)
    prev = datetime.strftime(prev, "%Y-%m-%d")
    next = search_date + timedelta(days=1)
    next = datetime.strftime(next, "%Y-%m-%d")
    try:
        schedule = Schedule.objects.filter(date=search_date)
        games = []
        for item in schedule:
            try:
                game_data = GameData.objects.get(scheduled_id=item.id)
            except Exception as e:
                game_data = "Game Not Played. Please check back later"
                print(e)
            games.append({"schedule": item, "game_data": game_data})
        if not schedule:
            context = {
                'search_date': date,
                'prev': prev,
                'next': next,
                'date': datetime.strftime(search_date, '%A %d %B'),
                'message': 'There are currently no games on the selected date. Please check another.',
            }
        else:
            context = {
                'search_date': date,
                'prev': prev,
                'next': next,
                'date': datetime.strftime(search_date, '%A %d %B'),
                'games': games,
            }
    except Exception as e:
        context = {
            'search_date': date,
            'prev': prev,
            'next': next,
            'date': datetime.strftime(search_date, '%A %d %B'),
            'message': 'There are currently no games on the selected date. Please check another.',
        }
    return render(request, template, context)
