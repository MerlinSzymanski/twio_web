# Generated by Django 3.0.3 on 2020-12-11 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0008_auto_20201211_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer_table',
            name='final_file',
            field=models.FileField(blank=True, null=True, upload_to='trainer_tables'),
        ),
    ]
