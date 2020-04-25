# Generated by Django 3.0.3 on 2020-04-24 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20200424_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='trainer_email',
            field=models.CharField(default='Hier die Email für die Website', max_length=150),
        ),
        migrations.AddField(
            model_name='trainer',
            name='trainer_telnr',
            field=models.CharField(default='Hier die Nummer für die Website', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 23, 57, 36, 931786)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 23, 57, 36, 931771)),
        ),
        migrations.AlterField(
            model_name='message',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 23, 57, 36, 932133)),
        ),
        migrations.AlterField(
            model_name='session',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2020, 4, 24, 23, 57, 36, 931424)),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2020, 4, 24, 23, 57, 36, 931397)),
        ),
    ]
