# Generated by Django 2.2.1 on 2019-05-16 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('Comment_ID', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('Movie_ID', models.IntegerField()),
                ('Context', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('Movie_ID', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('Title', models.CharField(default='', max_length=255)),
                ('Year', models.IntegerField()),
                ('Rated', models.BooleanField()),
                ('Released', models.DateField()),
                ('Runtime', models.IntegerField()),
                ('Genre', models.CharField(default='', max_length=255)),
                ('Director', models.CharField(default='', max_length=255)),
                ('Writer', models.CharField(default='', max_length=255)),
                ('Actors', models.CharField(default='', max_length=255)),
                ('Plot', models.CharField(default='', max_length=255)),
                ('Language', models.CharField(default='', max_length=255)),
                ('Awards', models.CharField(default='', max_length=255)),
                ('Poster', models.CharField(default='', max_length=255)),
                ('Ratings', models.CharField(default='', max_length=255)),
                ('Metascore', models.CharField(default='', max_length=255)),
                ('imdbRating', models.FloatField()),
                ('imdbVotes', models.IntegerField()),
                ('imdbID', models.CharField(default='', max_length=255)),
                ('Type', models.CharField(default='', max_length=25)),
                ('DVD', models.DateField()),
                ('BoxOffice', models.CharField(default='', max_length=255)),
                ('Production', models.CharField(default='', max_length=255)),
                ('Website', models.CharField(default='', max_length=255)),
                ('Response', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
