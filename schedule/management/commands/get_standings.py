from django.core.management.base import BaseCommand, CommandError
from teams.models import Team, Conference, Division
from django.core.exceptions import ObjectDoesNotExist
import requests
from django.conf import settings
import json


class Command(BaseCommand):
    help = 'Get current standings'

    def handle(self, *args, **options):
        url = f'https://api.sportradar.us/nba/trial/v7/en/seasons/2020/PRE/standings.json?api_key={settings.API_KEY}'
        response = requests.get(url)
        standings = response.json()
        for data in standings['conferences']:
            try:
                conference = Conference.objects.get(pk=data['id'])
            except ObjectDoesNotExist:
                conference = Conference(
                    name=data['name'],
                    id=data['id'],
                    alias=data['alias'],
                )
                conference.save()
                print('Conference Saved')
            for div in data['divisions']:
                try:
                    division = Division.objects.get(pk=div['id'])
                except ObjectDoesNotExist:
                    division = Division(
                        name=div['name'],
                        id=div['id'],
                        alias=div['alias'],
                        conference=Conference.objects.get(pk=data['id'])
                    )
                    division.save()
                    print('Division Save')
                for team in div['teams']:
                    try:
                        team_data = Team.objects.get(alias=team['name'])
                        team_data.conference = Conference.objects.get(
                            pk=conference.id)
                        team_data.division = Division.objects.get(pk=division.id)
                        team_data.wins = team['wins']
                        team_data.loses = team['losses']
                        team_data.win_pct = team['win_pct']
                        team_data.div_rank = team['calc_rank']['div_rank']
                        team_data.conf_rank = team['calc_rank']['conf_rank']
                        team_data.save()
                        team_data.calc_average()
                        print(f'Team updated {team_data.name}')
                    except Exception as e:
                        print(f'{e} - {team}')
