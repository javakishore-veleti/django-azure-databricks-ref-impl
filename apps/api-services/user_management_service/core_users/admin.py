from django.contrib import admin

from core_users.models import AppUser, AppUserProfile

# Register your models here.
admin.site.register(AppUser)
admin.site.register(AppUserProfile)