# Generated by Django 3.1.4 on 2020-12-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254, unique=True)),
                ('alias', models.CharField(max_length=20)),
                ('ratings_home', models.JSONField(default=list)),
                ('ratings_away', models.JSONField(default=list)),
                ('home_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('away_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
