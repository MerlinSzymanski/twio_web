# Generated by Django 3.0.3 on 2020-09-29 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20200929_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='gezahlt',
            field=models.BooleanField(default=False, verbose_name='Beitrag gezahlt'),
        ),
        migrations.AddField(
            model_name='participant',
            name='part',
            field=models.BooleanField(default=False, verbose_name='Teilgenommen'),
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Adresse'),
        ),
        migrations.AddField(
            model_name='profile',
            name='beitrag',
            field=models.IntegerField(default=20, verbose_name='Beitragshöhe'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Geburtstag'),
        ),
        migrations.AddField(
            model_name='profile',
            name='ermaessigt',
            field=models.BooleanField(default=False, verbose_name='Ermäßigt?'),
        ),
        migrations.AddField(
            model_name='profile',
            name='mandatsref',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Mandatsreferenz'),
        ),
        migrations.AddField(
            model_name='profile',
            name='membership_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Kündigung zum'),
        ),
        migrations.AddField(
            model_name='profile',
            name='membership_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Beginn der Mitgliedschaft'),
        ),
        migrations.AddField(
            model_name='profile',
            name='notes_chairman',
            field=models.TextField(blank=True, null=True, verbose_name='Notizen für den Vorstand'),
        ),
        migrations.AddField(
            model_name='profile',
            name='notes_trainer',
            field=models.TextField(blank=True, null=True, verbose_name='Notizen für den/die Trainer*in'),
        ),
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(default='w', max_length=1, verbose_name='Geschlecht'),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('ordentlich', 'Ordentliches Mitglied'), ('fördernd', 'Förderndes Mitglied'), ('pausiert', 'Pausiertes Mitglied')], default='Ordentliches Mitglied', max_length=40),
        ),
        migrations.AddField(
            model_name='profile',
            name='telephone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telephone'),
        ),
        migrations.AddField(
            model_name='profile',
            name='zahlungsart',
            field=models.CharField(choices=[('sepa', 'SEPA'), ('da', 'Dauerauftrag'), ('transfer', 'Überweisung')], default='SEPA', max_length=30, verbose_name='Zahlungsart'),
        ),
        migrations.AlterField(
            model_name='event',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 19, 29, 47, 796769), verbose_name='Anmeldung/Abmeldung bis'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 19, 29, 47, 796802), verbose_name='Datum Ende'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 19, 29, 47, 796789), verbose_name='Datum Beginn'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 19, 29, 47, 800182)),
        ),
    ]
