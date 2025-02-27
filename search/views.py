from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog.models import Blog
from search.serializer import SearchSuggestionsSerializer, SearchSerializer


class SearchBlogView(ListAPIView):
    serializer_class = SearchSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        title = self.request.query_params.get('title', '')
        content = self.request.query_params.get('content', '')

        queryset = Blog.objects.all()

        if title and self.request.user.is_authenticated:
            self.request.user.search.get_or_create(title=title)

        return queryset.filter(Q(title__icontains=title) & Q(content__icontains=content))


class SearchSuggestionsView(ListAPIView):
    serializer_class = SearchSuggestionsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        title = self.request.query_params.get('title', '')

        if not title:
            return self.request.user.search.all().order_by('-created_at').values_list('title', flat=True)[:5]

        return Blog.objects.filter(title__icontains=title).values_list('title', flat=True)[:5]

    def list(self, request, *args, **kwargs):
        return Response(list(self.get_queryset()))
