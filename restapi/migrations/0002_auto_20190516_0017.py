# Generated by Django 2.2.1 on 2019-05-16 00:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='Comment_ID',
            field=models.AutoField(default=uuid.uuid1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movies',
            name='Movie_ID',
            field=models.AutoField(default=uuid.uuid1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movies',
            name='Poster',
            field=models.URLField(),
        ),
    ]