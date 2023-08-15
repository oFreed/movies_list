from django.db import models


class Actor(models.Model):
    name = models.CharField(
        max_length=50
    )


class Director(models.Model):
    name = models.CharField(
        max_length=50
    )


class Genre(models.Model):
    name = models.CharField(
        max_length=50
    )


class Movie(models.Model):
    name = models.CharField(
        max_length=50
    )
    desc = models.CharField(
        max_length=250
    )
    image_url = models.URLField(
    )
    thumb_url = models.URLField(
    )
    imdb_url = models.CharField(
        max_length=150
    )
    rating = models.FloatField(
    )
    year = models.IntegerField(
    )
    actors = models.ManyToManyField(
        "Actor"
    )
    genre = models.ManyToManyField(
        "Genre"
    )
    directors = models.ManyToManyField(
        "Director"
    )
