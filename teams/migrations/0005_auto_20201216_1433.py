# Generated by Django 3.1.4 on 2020-12-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20201216_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='alias',
            field=models.CharField(default='', max_length=26),
        ),
        migrations.AddField(
            model_name='division',
            name='alias',
            field=models.CharField(default='', max_length=26),
        ),
    ]
