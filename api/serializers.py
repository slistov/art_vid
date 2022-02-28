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


# class ObjectTypeField(serializers.Field):
#     def get_attribute(self, instance):
#         return instance
#     def to_representation(self, instance):
#         return instance # ContentType(self).model

class CommentSerializer(ItemOwnedByUser):

    class Meta:
        model = Comment
        fields = '__all__' 
        # ['id', 'user', 'user_id', 'object_type', 'content_type', 'object_id', 'comment']

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