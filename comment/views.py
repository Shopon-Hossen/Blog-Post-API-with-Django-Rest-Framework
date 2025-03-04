from comment.serializer import CommentSerializer
from comment.models import Comment
from blog.models import Blog
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView
)
from django.shortcuts import get_object_or_404


class BaseCommentView:
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Comment.objects.all()


class CreateCommentView(BaseCommentView, CreateAPIView):
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DeleteCommentView(BaseCommentView, DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)


class ListCommentView(BaseCommentView, ListAPIView):
    permission_classes = [AllowAny]

    def get_queryset(self):
        blog_id = self.request.query_params.get('blog_id')
        blog = get_object_or_404(Blog, id=blog_id)
        return blog.comments.all()
