from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name',
                  'password', 'date_of_birth', 'is_verified', 'is_moderator']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id', 'is_verified', 'is_moderator']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name',
                  'date_of_birth', 'is_verified', 'is_moderator']
        read_only_fields = ['id', 'email', 'is_verified', 'is_moderator']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_verified']
        read_only_fields = ['id', 'email', 'is_verified']
