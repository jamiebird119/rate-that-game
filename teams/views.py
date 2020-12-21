from django.shortcuts import render
from .models import Team, Division, Conference
from schedule.models import Schedule
from datetime import datetime, timedelta, date

# Create your views here.


def standings(request, search):
    template = 'teams/standings.html'
    data = {}
    if search == "conf":
        confer = Conference.objects.all()
        for conf in confer:
            teams = conf.team_set.order_by('conf_rank')
            data[conf.name] = teams
    if search == 'div':
        division = Division.objects.all()
        for div in division:
            teams = div.team_set.order_by('div_rank')
            data[div.name] = teams
    context = {
        'data': data,
        'search': search,
    }
    return render(request, template, context)


def team_info(request, alias):
    team = Team.objects.get(alias=alias)
    template = 'teams/team.html'
    today = date.today()
    home = []
    away = []
    for key in team.ratings_home.keys():
        scheduled = Schedule.objects.get(id=key)
        game_data = scheduled.gamedata_set.get()
        if scheduled.date >= today - timedelta(days=14):
            home.append(
                {id: game_data}
            )
    for key in team.ratings_away.keys():
        scheduled = Schedule.objects.get(id=key)
        game_data = scheduled.gamedata_set.get()
        if scheduled.date >= today - timedelta(days=7):
            away.append(
                {id: game_data}
            )
    games = {
        'home': home,
        'away': away,
    }
    context = {
        'team': team,
        'games': games
    }
    return render(request, template, context)
