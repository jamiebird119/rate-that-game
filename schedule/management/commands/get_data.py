from django.core.management.base import BaseCommand, CommandError
from schedule.models import Schedule, GameData
from teams.models import Team
from datetime import date, timedelta
from django.conf import settings
import requests
import json
from json.decoder import JSONDecodeError
import time


class Command(BaseCommand):
    help = 'Find and save game data for yesterdays games'

    def handle(self, *args, **options):
        yesterday = date.today() - timedelta(days=1)
        try:
            games = Schedule.objects.filter(date=yesterday)
            for game in games:
                time.sleep(1)
                url = f"https://api.sportradar.us/nba/trial/v7/en/games/{game.id}/boxscore.json?api_key={settings.API_KEY}"
                self.stdout.write(url)
                if not game.game_data_saved:
                    try:
                        response = requests.get(url)
                        game_data = response.json()
                        game_data = GameData(
                            scheduled=Schedule.objects.get(pk=game.id),
                            lead_changes=game_data['lead_changes'],
                            teams_string=f'{game.home.name} vs {game.away.name}',
                            home_points=game_data['home']['points'],
                            away_points=game_data['away']['points'],
                            home_scoring=game_data['home']['scoring'],
                            away_scoring=game_data['away']['scoring'],
                        )
                        game_data.get_rating()
                        game_data.check_OT()
                        time.sleep(1)
                        self.stdout.write('Game Data Saved correctly ')
                        home_team = Team.objects.get(name=game.home.name)
                        home_team.ratings_home[game.id] = game_data.rating
                        home_team.calc_rating()
                        home_team.save()
                        away_team = Team.objects.get(name=game.away.name)
                        away_team.ratings_away[game.id] = game_data.rating
                        away_team.calc_rating()
                        away_team.save()
                        self.stdout.write('Team Ratings saved correctly ')
                        game.game_data_saved = True
                        game.save()
                        with open('success.json') as json_file:
                            try:
                                old_data = json.load(json_file)
                                old_data[game.id] = game_data.teams_string
                                with open('success.json', 'w') as jfile:
                                    json.dump(old_data, jfile)
                            except JSONDecodeError:
                                y = {game.id: game_data.teams_string}
                                with open('success.json', 'w') as jfile:
                                    json.dump(y, jfile)
                    except Exception as e:
                        print(f'Error as {e} ')
                        # Get it to save error and ids to file
                        with open('error.json') as json_file:
                            try:
                                old_data = json.load(json_file)
                                old_data[game.id] = e
                                with open('error.json', 'w') as jfile:
                                    json.dump(old_data, jfile)
                            except JSONDecodeError:
                                y = {game.id: e}
                                with open('error.json', 'w') as jfile:
                                    json.dump(y, jfile)
        except Schedule.DoesNotExist:
            raise CommandError('Game does not exist')

    
