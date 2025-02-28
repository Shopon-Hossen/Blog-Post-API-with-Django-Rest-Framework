from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from tag.models import Tag
from tag.serializer import TagSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)


class TagCreateView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagAddView(APIView):
    def post(self, request):
        pass
