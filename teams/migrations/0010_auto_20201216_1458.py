# Generated by Django 3.1.4 on 2020-12-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_auto_20201216_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='division',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]