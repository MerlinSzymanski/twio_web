# Generated by Django 3.0.3 on 2021-05-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interested', '0010_auto_20210514_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmerch',
            name='price',
            field=models.CharField(max_length=10, verbose_name='Preis'),
        ),
    ]
