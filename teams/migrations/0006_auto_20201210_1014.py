# Generated by Django 3.1.4 on 2020-12-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20201207_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='ratings_away',
            field=models.JSONField(blank=True, default=[]),
        ),
        migrations.AddField(
            model_name='team',
            name='ratings_home',
            field=models.JSONField(blank=True, default=[]),
        ),
    ]