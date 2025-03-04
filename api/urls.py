from django.urls import path, include


urlpatterns = [
    path('account/', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('search/', include('search.urls')),
    path('comment/', include('comment.urls')),
    path('tag/', include('tag.urls')),
]
