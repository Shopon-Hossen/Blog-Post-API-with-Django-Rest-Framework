from rest_framework import serializers
from tag.models import Tag
from tag.utils import get_or_create_tag
from blog.models import Blog


class TagSerializer(serializers.Serializer):
    tags = serializers.ListField(
        child=serializers.CharField(max_length=50, allow_blank=False)
    )
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())


class TagCreateSerializer(serializers.Serializer):
    tags = serializers.ListField(
        child=serializers.CharField(max_length=50, allow_blank=False)
    )
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())

    def create(self, validated_data):
        blog = validated_data.get('blog')
        tags = validated_data.get('tags')

        tags_obj = get_or_create_tag(tags)
        blog.tags.add(*tags_obj)
        return blog

    def to_representation(self, instance):
        return {
            "tags": [tag.name for tag in instance.tags.all()],
            "blog": instance.id
        }
