# Generated by Django 3.1.4 on 2020-12-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20201207_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='gameData_saved',
            field=models.BooleanField(default=False),
        ),
    ]
