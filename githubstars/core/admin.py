from django.contrib import admin
from .models import Repositorie


@admin.register(Repositorie)
class RepositorieAdmin(admin.ModelAdmin):
    """ Competition admin """
    list_display = ('repositorie_id', 'repositorie_name', 'repositorie_language',)
    list_display_links = ('repositorie_id', 'repositorie_name', 'repositorie_language')
    list_filter = ('repositorie_language',)
