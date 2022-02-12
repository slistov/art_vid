from tkinter import CASCADE, Text
from typing import cast
from django.db import models
from django.forms import CharField, URLField


class User(models.Model):
    id = models.IntegerField()
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.id + self.email


class Article(models.Model):
    id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=250)
    article = Text()

    def __str__(self):
        return self.name


class Video(models.Model):
    id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=250)
    url = URLField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=250)
    article = Text()

    def __str__(self):
        return self.name
