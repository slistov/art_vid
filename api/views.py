#from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.models import Article, Video
from api.serializers import ArticleSerializer, VideoSerializer, CommentSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows article to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows video to be viewed or edited.
    """
    queryset = Video.objects.all().order_by('-id')
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comment to be viewed or edited.
    """
    queryset = Video.objects.all().order_by('id')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]