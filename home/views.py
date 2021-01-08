from django.shortcuts import render
from datetime import date, timedelta
from teams.models import Team
from schedule.models import GameData, Schedule


# home page
def index(request):
    template = 'home/index.html'
    today = date.today()
    last_two_weeks = [str(today-timedelta(days=14)), str(today)]

    # 5star rated games from the last two weeks
    five_star = GameData.objects.filter(
        rating=5, scheduled__date__range=last_two_weeks)

    # top rated games last two weeks - not shown on latest version
    games_lasttwoweeks = GameData.objects.filter(
        scheduled__date__range=last_two_weeks)
    top_rated = games_lasttwoweeks.order_by("-rating")[: 5]
    context = {
        'today': today,
        'five_star': five_star,
        'top_rated': top_rated
    }

    return render(request, template, context)
