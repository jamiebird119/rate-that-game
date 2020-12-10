from .models import Schedule, GameData
from teams.models import Team
from datetime import date, timedelta
from django.conf import settings
import requests
import json
import time


def my_cron_job():
    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    games = Schedule.objects.filter(date=yesterday)

    for game in games:
        time.sleep(1)
        url = "https://api.sportradar.us/nba/trial/v7/en/games/{game.id}/boxscore.json?api_key={settings.API_KEY}"
        try:
            response = requests.get(url)
            game_data = response.json()
            data = {
                'scheduled': game.id,
                'lead_changes': game_data['lead_changes'],
                'teams_string': f'{game.home.name} vs {game.away.name}',
                'home_points':  game_data['home']['points'],
                'away_points': game_data['away']['points'],
                'home_scoring': game_data['home']['scoring'],
                'away_scoring': game_data['away']['scoring'],
            }
            game_data = GameData.objects.create(data)
            game_data.get_rating()
            game_data.check_OT()
            print('Game Data Saved correctly ')
            home_team = Team(name=game.home.name)
            home_team.add_home_rating(game.id, game_data.rating)
            away_team = Team(name=game.away.name)
            away_team.add_away_rating(game.id, game_data.rating)
            print('Team Ratings saved correctly ')
            game.game_data_saved = True
            game.save()

        except Exception as e:
            # Get it to save error and ids to file
            with open('error.json') as json_file:
                data = json.load(json_file)
                temp = data or []
                y = {game.id, e}

                # appending data to emp_details
                temp.append(y)
            print('Error as e')