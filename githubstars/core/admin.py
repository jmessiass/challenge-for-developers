from django.contrib import admin
from .models import Repository


@admin.register(Repository)
class RepositorieAdmin(admin.ModelAdmin):
    """ Competition admin """
    list_display = ('repository_id', 'name', 'language',)
    list_display_links = ('repository_id', 'name', 'language')
    list_filter = ('language',)
