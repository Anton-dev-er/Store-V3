from django.contrib import admin
from . import models


class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'display_name', 'join_date')
    list_display_links = ('email',)


admin.site.register(models.AuthUser, AuthUserAdmin)


