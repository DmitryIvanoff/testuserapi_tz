from django.contrib import admin

from apps.users.models import User,Color


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass
