# Generated by Django 3.2.22 on 2023-11-13 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='description',
            field=models.TextField(default='Description not provided'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='reps',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='sets',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
