from django.contrib import admin

from .models import *


@admin.register(PublicLink)
class PublicLinkAdmin(admin.ModelAdmin):
    fields = ('URL', 'file')
    list_display = ('URL', 'file', 'generationDate')
    list_filter = ('file', )


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fields = ('fileName', 'extension', 'content', 'directory')
    list_display = ('fileName', 'extension', 'directory', 'isFavourite', 'inBin')
    list_filter = ('extension', 'directory', 'isFavourite', 'inBin',)
    search_fields = ('fileName', 'extension')
    actions = ['make_favourite', 'unmake_favourite', 'move_to_bin', 'restore_from_bin']

    def make_favourite(self, request, queryset):
        queryset.update(isFavourite=True)

    def unmake_favourite(self, request, queryset):
        queryset.update(isFavourite=False)

    def move_to_bin(self, request, queryset):
        queryset.update(inBin=True)

    def restore_from_bin(self, request, queryset):
        queryset.update(inBin=False)


class InLineFile(admin.TabularInline):
    model = File
    extra = 0


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    inlines = [InLineFile]
    fields = ('user', 'directoryName', )
    list_display = ('directoryName', 'user', )
    list_filter = ('user', )
    search_fields = ('directoryName', )
