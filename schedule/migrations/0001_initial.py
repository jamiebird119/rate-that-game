# Generated by Django 3.1.3 on 2020-11-25 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('away', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Away', to='teams.team')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Home', to='teams.team')),
            ],
        ),
    ]
