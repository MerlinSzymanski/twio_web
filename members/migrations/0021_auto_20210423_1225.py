# Generated by Django 3.0.3 on 2021-04-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0020_auto_20201127_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titel'),
        ),
    ]
