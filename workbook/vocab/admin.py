from django.contrib import admin

from vocab.models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Word, WordAdmin)
