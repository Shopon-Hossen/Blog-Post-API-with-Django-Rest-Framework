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
    BlogDetailSerializer,
)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SimilarView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, blog_id, *args, **kwargs):
        blog = Blog.objects.filter(id=blog_id).first()
        if not blog:
            return Response({
                "error": "Blog not found"
            }, status=status.HTTP_404_NOT_FOUND)
        
        similar_blogs = blog.get_similar_blogs()
        serializer = BlogListSerializer(similar_blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BaseBlogView:
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]


class BlogCreateView(BaseBlogView, CreateAPIView):
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogListView(BaseBlogView, ListAPIView):
    serializer_class = BlogListSerializer
    ordering = ['-created_at']


class BlogDetailView(BaseBlogView, RetrieveAPIView):
    serializer_class = BlogDetailSerializer


class BlogDeleteView(BaseBlogView, DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


class BlogUpdateView(BaseBlogView, UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)
