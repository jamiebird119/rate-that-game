# Generated by Django 3.1.4 on 2020-12-07 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20201207_1431'),
        ('schedule', '0007_gamedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='away',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='teams.team', to_field='name'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='teams.team', to_field='name'),
        ),
    ]