from django.urls import path
from like import views

urlpatterns = [
    path('create/', views.LikeCreateView.as_view(), name='like_create'),
    path('delete/', views.LikeDeleteView.as_view(), name='like_delete'),
]
