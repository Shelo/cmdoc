from django.contrib import admin

from section import models

class SectionAdmin(admin.ModelAdmin):
    list_display = ['short_content', 'document_title', 'owner', 'position',
                    'last_modified', 'message', 'modifier', 'editing']

admin.site.register(models.Section, SectionAdmin)
