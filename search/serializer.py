from rest_framework import serializers
from search.models import Search


class SearchSuggestionsSerializer(serializers.Serializer):
    title = serializers.CharField()


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'
        read_only_fields = ['user']
