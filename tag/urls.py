from django.urls import path
from tag import views

urlpatterns = [
    path('create/', views.TagCreateView.as_view(), name='create_tag'),
]
