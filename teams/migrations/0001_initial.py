# Generated by Django 3.1.3 on 2020-11-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('alias', models.CharField(max_length=20)),
                ('home_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3)),
                ('away_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
