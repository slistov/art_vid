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

    class Meta:
        fields = ['user', 'user_id']


class CommentSimplifiedSerializer(ItemOwnedByUser):
    
    class Meta(ItemOwnedByUser.Meta):
        model = Comment
        fields = ['id', 'comment'] + ItemOwnedByUser.Meta.fields


class ItemCommentedByUser(serializers.ModelSerializer):
    comments = CommentSimplifiedSerializer(many=True)

    class Meta:
        fields = ['comments']


class ArticleSerializer(ItemOwnedByUser, ItemCommentedByUser):

    class Meta:
        model = Article
        fields = (
            ['id', 'name', 'article'] + 
            ItemOwnedByUser.Meta.fields + 
            ItemCommentedByUser.Meta.fields
        )



class VideoSerializer(ItemOwnedByUser, ItemCommentedByUser):
    class Meta:
        model = Video
        fields = (
            ['id', 'name', 'url'] + 
            ItemOwnedByUser.Meta.fields + 
            ItemCommentedByUser.Meta.fields
        )


class CommentSerializer(CommentSimplifiedSerializer):

    class Meta(CommentSimplifiedSerializer.Meta):
        fields = CommentSimplifiedSerializer.Meta.fields + [
            'object_id',
            'content_type'
        ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        content_type_id = representation.pop('content_type')
        object_type_str = ContentType.objects.get_for_id(content_type_id).model
        representation['object_type'] = object_type_str
        return representation

    def to_internal_value(self, data):
        object_type_str = data.pop('object_type')
        content_type_id = ContentType.objects.get(model=object_type_str).id
        data['content_type'] = content_type_id
        return super().to_internal_value(data)