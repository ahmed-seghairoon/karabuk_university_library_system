from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from . import models

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id',"username", "email", "first_name","last_name","role", "is_staff")

    list_filter = ("role","is_staff", "is_superuser", "is_active", "groups")

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name","last_name","email","username","role", "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name","last_name","email","role")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )