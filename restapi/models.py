# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db import models
from datetime import date

# Create your models here.
class Movies(models.Model):
    id=models.AutoField(primary_key=True,default=None)
    Title=models.CharField(max_length=255,default="")
    Year=models.CharField(max_length=255,default="")
    Rated=models.CharField(max_length=255,default="")
    Released=models.CharField(max_length=255,default="")
    Runtime=models.CharField(max_length=255,default="")
    Genre=models.CharField(max_length=255,default="")
    Director=models.CharField(max_length=255,default="")
    Writer=models.CharField(max_length=255,default="")
    Actors=models.CharField(max_length=255,default="")
    Plot=models.CharField(max_length=255,default="")
    Language=models.CharField(max_length=255,default="")
    Country=models.CharField(max_length=255,default="")
    Awards=models.CharField(max_length=255,default="")
    Poster=models.URLField()
    Ratings=models.CharField(max_length=255,default="")
    Metascore=models.CharField(max_length=255,default="")
    imdbRating=models.CharField(max_length=255,default="")
    imdbVotes=models.CharField(max_length=255,default="")
    imdbID=models.CharField(max_length=255,default="")
    Type=models.CharField(max_length=25,default="")
    DVD=models.CharField(max_length=255,default="")
    BoxOffice=models.CharField(max_length=255,default="")
    Production=models.CharField(max_length=255,default="")
    Website=models.CharField(max_length=255,default="")
    totalSeasons=models.CharField(max_length=255,default="")
    Response=models.BooleanField()


class Comments(models.Model):
    Movie_ID=models.IntegerField()
    Context=models.CharField(max_length=255,default="")
    Date = models.DateField(default=date.today)