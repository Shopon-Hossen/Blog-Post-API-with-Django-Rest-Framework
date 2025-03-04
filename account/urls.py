from django.urls import path
from account import views


urlpatterns = [
    path('', views.GetUserView.as_view(), name='user'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('update-user/', views.UpdateUserView.as_view(), name='update_user'),
    path('change-password/', views.ChangePasswordView.as_view(),
         name='change_password'),
    path('user/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('user/<int:pk>/blogs/', views.UserBlogListView.as_view(), name='user_blogs'),
]
