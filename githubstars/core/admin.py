from django.contrib import admin
from .models import Repositorie


@admin.register(Repositorie)
class RepositorieAdmin(admin.ModelAdmin):
    """ Competition admin """
    list_display = ('repositorie_id', 'name', 'language',)
    list_display_links = ('repositorie_id', 'name', 'language')
    list_filter = ('language',)
