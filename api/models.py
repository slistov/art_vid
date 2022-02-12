from tkinter import CASCADE, Text
from typing import cast
from django.db import models
from django.forms import CharField, URLField


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=250)
    article = models.TextField(default='')

    def __str__(self):
        return self.name


class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=250)
    url = models.URLField(default='')

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.TextChoices('Для статьи или для видео?', 'Article Video')
    comment = models.TextField('Текст комментария', default='')

    def __str__(self):
        return self.name