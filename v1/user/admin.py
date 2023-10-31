<<<<<<< HEAD
from django.contrib import admin

from v1.user.models import  User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone")


=======
from django.contrib import admin

from v1.user.models import  User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone")


>>>>>>> d51e158 (..)
