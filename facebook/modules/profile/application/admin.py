from django.contrib import admin

from facebook.modules.base import AdminBase

class RequestAdmin(AdminBase):
    list_display = ('id', '_application_id', '_to', '_from', '_data', '_message', '_created_time')
    readonly_fields = ('_graph', '_application_id', '_to', '_from', '_data', '_message', '_created_time')

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')
    readonly_fields = ('user', 'score')
    search_fields = ('user',)
    ordering = ['score']