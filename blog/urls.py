from django.urls import path
from blog import views


urlpatterns = [
    path('create/', views.BlogCreateView.as_view(), name='create_blog'),
    path('list/', views.BlogListView.as_view(), name='list_blog'),
    path('update/<int:pk>/', views.BlogUpdateView.as_view(), name='update_blog'),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(), name='detail_blog'),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name='delete_blog'),

]
