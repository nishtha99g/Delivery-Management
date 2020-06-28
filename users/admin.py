from django.contrib import admin
from .models import Profile


class ProfileItemInline(admin.TabularInline):
    model = Profile
    raw_id_fields = ['users']


class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'city', 'postcode', 'date_birth','shopkeeper']


admin.site.register(Profile, UserAdmin)
