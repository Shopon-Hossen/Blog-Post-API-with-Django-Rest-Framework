from django.contrib import admin
from tag.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Tag, TagAdmin)
