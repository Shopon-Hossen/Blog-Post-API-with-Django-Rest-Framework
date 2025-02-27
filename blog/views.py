from blog.models import Blog
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from blog.serializer import (
    BlogSerializer,
    BlogListSerializer,
)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)


class BaseBlogView:
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]


class CreateBlogView(BaseBlogView, CreateAPIView):
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogListView(BaseBlogView, ListAPIView):
    serializer_class = BlogListSerializer


class BlogDetailView(BaseBlogView, RetrieveAPIView):
    pass


class BlogDeleteView(BaseBlogView, DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


class BlogUpdateView(BaseBlogView, UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)
