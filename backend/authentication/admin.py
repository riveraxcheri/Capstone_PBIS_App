from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Student

class CustomUserAdmin(UserAdmin):
    pass

# Register your models here.
admin.site.register(User, CustomUserAdmin)
