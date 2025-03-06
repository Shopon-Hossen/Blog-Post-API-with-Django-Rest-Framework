from rest_framework.permissions import IsAuthenticated, AllowAny
from tag.serializer import TagCreateSerializer
from blog.models import Blog
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView
)
from tag.serializer import TagSerializer
from tag.utils import get_or_create_tag
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from blog.serializer import BlogListSerializer
from tag.models import Tag
from rest_framework.views import APIView


class SearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        tag_name = request.query_params.get('tag').lower()
        tag = get_object_or_404(Tag, name=tag_name)
        blogs = tag.blog_set.all()
        serializer = BlogListSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TagCreateSerializer

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


class TagDeleteView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer

    def delete(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, id=request.data.get(
            'blog'), author=request.user
        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tags = serializer.validated_data['tags']

        tags_obj = get_or_create_tag([tag.lower() for tag in tags])

        blog.tags.remove(*tags_obj)

        return Response({
            "blog": blog.id,
            "tags": [tag.name for tag in blog.tags.all()]
        }, status=status.HTTP_200_OK)
