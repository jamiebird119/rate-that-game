from django.urls import path
from . import views


urlpatterns = [
    path('standings/<search>/', views.standings, name='standings'),
    path('team_info/<alias>/', views.team_info, name='team_info'),
]