from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'name')
    list_filter = ('email', 'username',
                   'name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('id', 'email', 'username', 'name',
                    'is_active', 'is_staff', 'is_superuser')
    fieldsets = ((None, {'fields': ('email', 'username', 'name',)}), ('Permissions', {
                 'fields': ('is_staff', 'is_active')}))

    add_fieldsets = ((None, {'classes': ('wide',), 'fields': (
        'email', 'username', 'name', 'role', 'password1', 'password2', 'is_active', 'is_staff')}),)


admin.site.register(User, UserAdminConfig)
