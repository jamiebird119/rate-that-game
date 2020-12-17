from django.shortcuts import render
from .models import Team, Division, Conference

# Create your views here.


def standings(request, search):
    template = 'teams/standings.html'
    data = {}
    if search == "conf":
        confer = Conference.objects.all()
        for conf in confer:
            teams = conf.team_set.order_by('conf_rank')
            data[conf.name] = teams
    context = {
        'data': data,
        'search': search,
    }
    return render(request, template, context)
