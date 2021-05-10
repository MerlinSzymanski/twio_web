# Generated by Django 3.0.3 on 2021-05-10 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interested', '0006_eventparticipant_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventparticipant',
            name='merch_size',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Größe'),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='merch_wanted',
            field=models.BooleanField(default=False, verbose_name='Merch bestellt'),
        ),
    ]
