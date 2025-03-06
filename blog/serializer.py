from rest_framework import serializers
from comment.serializer import CommentSerializer
from blog.models import Blog
from account.serializer import UserProfileSerializer


class BlogSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(source='likes.count', read_only=True)
    author = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['author']

    def get_author(self, obj):
        return UserProfileSerializer(obj.author).data


class BlogListSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(source='likes.count')
    tags = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'author', 'likes', 'tags', 'title', 'content', 'created_at']
        read_only_fields = ['author', 'tags', 'likes']

    def get_author(self, obj):
        return UserProfileSerializer(obj.author).data
    
    def get_tags(self, obj):
        tags = obj.tags.all()
        return [tag.name for tag in tags]


class BlogDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    likes = serializers.IntegerField(source='likes.count')

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['author', 'likes', 'comments', 'tags']

    def get_comments(self, obj):
        comments = obj.comments.all()[:10]
        return CommentSerializer(comments, many=True).data

    def get_tags(self, obj):
        tags = obj.tags.all()
        return [tag.name for tag in tags]

    def get_author(self, obj):
        return UserProfileSerializer(obj.author).data


# TODO: Create more serializer for blog app.
