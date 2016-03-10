from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post, UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model UserInfo
        fields = ('uuid', 'host', 'displayName', 'url', 'github')

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('identity', 'username', 'posts')



    
class PostSerializer(serializers.ModelSerializer):
    # TODO change source to = some user serializer with ID, host,displayname
    # url and github (see api protocols)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        
        fields = (
            'title', 'source', 'origin', 'description',
            'contentType', 'content', 'author', 'categories',
            'published', 'identity', 'visibility'
        )



    
