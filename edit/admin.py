from django.contrib import admin

from . import models

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'create_time', 'users_count']
    ordering = ('-create_time', )

admin.site.register(models.Document, DocumentAdmin)
