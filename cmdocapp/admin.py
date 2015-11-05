from django.contrib import admin

from . import models

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'create_time', 'users_count']

    ordering = ('-create_time', )

class SectionAdmin(admin.ModelAdmin):
    list_display = ['short_content', 'document_title', 'owner', 'position',
                    'last_modified', 'message', 'modifier', 'editing']

admin.site.register(models.Document, DocumentAdmin)
admin.site.register(models.Section, SectionAdmin)
