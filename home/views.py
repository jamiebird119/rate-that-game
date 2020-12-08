from django.shortcuts import render
from datetime import date
# Create your views here.


def index(request):
    template = 'home/index.html'
    today = date.today()
    context = {
        'today': today,
    }

    return render(request, template, context)
