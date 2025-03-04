from rest_framework import serializers
from comment.serializer import CommentSerializer
from blog.models import Blog
from account.serializer import UserListSerializer


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['author']


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'content', 'created_at']
        read_only_fields = ['author']


class BlogDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['author']

    def get_comments(self, obj):
        comments = obj.comments.all()[:10]
        return CommentSerializer(comments, many=True).data

    def get_tags(self, obj):
        tags = obj.tags.all()
        return [tag.name for tag in tags]

    def get_author(self, obj):
        return UserListSerializer(obj.author).data


# TODO: Create more serializer for blog app.
