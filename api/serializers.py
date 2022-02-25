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


class CommentSerializer(ItemOwnedByUser):
    # object_type = serializers.CharField(source='content_type.model')
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_id', 'content_type', 'object_id', 'comment']
    
    # def create(self, validated_data):
    #     # object_type = validated_data.pop('object_type')
    #     content_type = validated_data.pop('content_type')
    #     content_type = ContentType.objects.get(app_label='api', model='article')
    #     return Comment.objects.create(content_type=content_type, **validated_data)
    #     # return super().create(validated_data)
