from django.contrib import admin
from search.models import Search


class SearchAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'

admin.site.register(Search, SearchAdmin)