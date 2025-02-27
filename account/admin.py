from django.contrib import admin
from account.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'date_of_birth']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['date_of_birth']


admin.site.register(User, UserAdmin)
