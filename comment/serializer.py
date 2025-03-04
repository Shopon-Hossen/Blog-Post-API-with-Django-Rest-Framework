from rest_framework import serializers
from comment.models import Comment
from account.serializer import UserListSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'blog', 'created_at']
        read_only_fields = ['author']

    def get_author(self, obj):
        return UserListSerializer(obj.author).data
