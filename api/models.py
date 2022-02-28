from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User


class Article(models.Model):
    """
    Модель для сущности Article
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=250)
    article = models.TextField(default='')
    comments = GenericRelation('Comment')

    def __str__(self):
        return self.name


class Video(models.Model):
    """
    Модель для сущности Video
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=250)
    url = models.URLField(default='')
    comments = GenericRelation('Comment')

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    Сущность Comment. Полиморфная связь с Article и Video
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    comment = models.TextField('Текст комментария', default='')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    commented_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.comment