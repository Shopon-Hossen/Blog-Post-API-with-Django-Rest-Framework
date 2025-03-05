from rest_framework import serializers
from like.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, data):
        request = self.context.get('request')
        user = request.user if request else None
        post = data.get('post')
        if user and post and Like.objects.filter(user=user, post=post).exists():
            raise serializers.ValidationError(
                "You have already liked this post."
            )
        return data
