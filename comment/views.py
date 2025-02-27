from comment.serializer import CommentSerializer
from comment.models import Comment
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView
)


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
    def get_queryset(self):
        return Comment.objects.filter(blog=self.request.data['blog'])
