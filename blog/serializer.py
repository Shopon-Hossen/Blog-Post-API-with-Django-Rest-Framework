from rest_framework import serializers
from comment.serializer import CommentSerializer
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source="comment")

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['author']


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'created_at']
        read_only_fields = ['author']

# TODO: Create more serializer for blog app.