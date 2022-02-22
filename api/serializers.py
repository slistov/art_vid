from rest_framework import serializers
from api.models import Article, Video, Comment

# class CurrentUserDefault(object):
#     def set_context(self, serializer_field):
#         self.user_id = serializer_field.context['request'].user.id

#     def __call__(self):
#         return self.user_id

#     def __repr__(self):
#         return unicode_to_repr('%s()' % self.__class__.__name__)

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    user_id = serializers.IntegerField(
        read_only=True
    )
    comments = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='comment'
    )
    class Meta:
        model = Article
        fields = ['id', 'user', 'user_id', 'name', 'article', 'comments']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'user_id', 'name', 'url']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'comment']

