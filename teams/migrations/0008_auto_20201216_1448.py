# Generated by Django 3.1.4 on 2020-12-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_remove_team_calc_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='conf_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='div_rank',
            field=models.IntegerField(default=0),
        ),
    ]