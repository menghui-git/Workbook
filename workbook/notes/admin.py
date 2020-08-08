from django.contrib import admin

from notes.models import UserWord


class UserWordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'word', 'created_at')


admin.site.register(UserWord, UserWordAdmin)
