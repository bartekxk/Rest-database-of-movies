# Generated by Django 2.2.1 on 2019-05-23 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0007_movies_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='Released',
            field=models.CharField(default='', max_length=255),
        ),
    ]
