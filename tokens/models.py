from django.db import models

from tokens.validators import validate_token_key


class Token(models.Model):
    document = models.ForeignKey('edit.Document')
    key = models.CharField(max_length=50, primary_key=True, validators=[validate_token_key])
    value = models.TextField()

    class Meta:
        ordering = ['-document_id', 'key']

    def __str__(self):
        return self.key
