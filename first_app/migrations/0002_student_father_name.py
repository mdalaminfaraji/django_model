# Generated by Django 4.2.7 on 2023-12-09 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.TextField(default='Rohim'),
        ),
    ]
