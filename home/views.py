from django.shortcuts import render
from datetime import date, timedelta
from teams.models import Team
from schedule.models import GameData, Schedule
# Create your views here.


def index(request):
    template = 'home/index.html'
    today = date.today()
    five_star = GameData.objects.filter(rating=5, scheduled__date__range=[
                                        today, today-timedelta(days=14)])
    top_rated = GameData.objects.order_by("-rating")[:5]
    context = {
        'today': today,
        'five_star': five_star,
        'top_rated': top_rated
    }

    return render(request, template, context)
