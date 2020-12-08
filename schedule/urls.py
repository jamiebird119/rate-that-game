from django.urls import path
from . import views


urlpatterns = [
    path('search/<date>/', views.schedule_search, name='schedule_search'),
]