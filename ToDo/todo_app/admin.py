# todo_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TodoModel

admin.site.register(CustomUser, UserAdmin)
admin.site.register(TodoModel)
