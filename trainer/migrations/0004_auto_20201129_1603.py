# Generated by Django 3.0.3 on 2020-11-29 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0020_auto_20201127_0107'),
        ('trainer', '0003_auto_20201129_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table_entry',
            name='session',
        ),
        migrations.AddField(
            model_name='table_entry',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.Session'),
        ),
    ]
