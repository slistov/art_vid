from rest_framework import serializers
from api.models import Article, Video, Comment
from django.contrib.contenttypes.models import ContentType



class ItemOwnedByUser(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    user_id = serializers.IntegerField(
        read_only=True
    )

class ItemCommentedByUser(serializers.ModelSerializer):
    comments = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='comment'
    )


class ArticleSerializer(ItemOwnedByUser, ItemCommentedByUser):
    class Meta:
        model = Article
        fields = ['id', 'user', 'user_id', 'name', 'article', 'comments']


class VideoSerializer(ItemOwnedByUser, ItemCommentedByUser):
    class Meta:
        model = Video
        fields = ['id', 'user', 'user_id', 'name', 'url', 'comments']


class ObjectTypeField(serializers.Field):
    def get_attribute(self, instance):
        return 'get attrib'
    def to_representation(self, instance):
        return instance # ContentType(self).model

class CommentSerializer(ItemOwnedByUser):
    object_type = ObjectTypeField(source='content_type')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_id', 'object_type', 'content_type', 'object_id', 'comment']
