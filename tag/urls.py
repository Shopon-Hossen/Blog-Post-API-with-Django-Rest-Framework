from django.urls import path
from tag import views

urlpatterns = [
    path('create/', views.TagCreateView.as_view(), name='create_tag'),
    path('delete/', views.TagDeleteView.as_view(), name='delete_tag'),
    path('search/', views.SearchView.as_view(), name='search_tag'),
]
