from django.contrib import admin

# Register your models here.
from backend.apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'id')
