from django.contrib import admin

from tokens import models

class TokenAdmin(admin.ModelAdmin):
    list_display = ['key', 'value', 'document']

admin.site.register(models.Token, TokenAdmin)
