from django.contrib import admin
from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'author']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Blog, BlogAdmin)


