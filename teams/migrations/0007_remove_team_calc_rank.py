# Generated by Django 3.1.4 on 2020-12-16 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20201216_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='calc_rank',
        ),
    ]