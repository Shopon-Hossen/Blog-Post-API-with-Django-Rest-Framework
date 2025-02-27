from django.contrib import admin
from comment.models import Comment



class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'blog']
    search_fields = ['author', 'content']
    list_filter = ['created_at']

admin.site.register(Comment, CommentAdmin)

