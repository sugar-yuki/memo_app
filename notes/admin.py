from django.contrib import admin
from .models import Note, Tag

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('tags',)
    ordering = ('-created_at',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)