# Generated by Django 4.2 on 2023-05-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='attempts',
            field=models.IntegerField(default=3),
        ),
    ]
