from django.urls import path
from search import views


urlpatterns = [
    path('', views.SearchBlogView.as_view(), name='search'),
    path('suggestion/', views.SearchSuggestionsView.as_view(), name='search_suggestions'),
]