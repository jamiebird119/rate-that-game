from django.urls import path
from . import views


urlpatterns = [
    path('standings/<search>/', views.standings, name='standings'),
]