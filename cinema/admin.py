from django.contrib import admin

from cinema.models import User, Post

# Register your models here.

@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "name")

admin.site.register(Post)
