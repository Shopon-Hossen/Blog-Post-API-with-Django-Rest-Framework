from django.urls import path
from comment import views


urlpatterns = [
    path('list/', views.ListCommentView.as_view(), name='list_comment'),
    path('create/', views.CreateCommentView.as_view(), name='create_comment'),
    path('delete/<int:pk>/', views.DeleteCommentView.as_view(), name='delete_comment'),
]
