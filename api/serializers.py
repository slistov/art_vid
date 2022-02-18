from rest_framework import serializers
from api.models import User, Article, Video, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']


class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='comment'
    )
    class Meta:
        model = Article
        fields = ['id', 'user_id', 'name', 'article', 'comments']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'user_id', 'name', 'url']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'comment']

