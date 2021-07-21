from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.urls import path
from users.models import AuthUser
from users.forms import UserCreationForm


# Register your models here.
@admin.register(AuthUser)
class AuthUserAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'profile_avatar')
    fieldsets = (
        (None, {'fields': ('email',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email'),
        }),
    )
    search_fields = ('first_name', 'last_name', 'email')
    add_form = UserCreationForm

    def get_urls(self):
        return super(BaseUserAdmin, self).get_urls()
