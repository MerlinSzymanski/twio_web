# Generated by Django 3.0.3 on 2020-11-27 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Datum')),
                ('credits', models.IntegerField(blank=True, null=True, verbose_name='Lernpunkte')),
                ('certificate', models.FileField(blank=True, null=True, upload_to='trainer_stuff', verbose_name='Teilnahmebestätigung')),
            ],
        ),
    ]
