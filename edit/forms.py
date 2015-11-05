from django import forms
from edit import models

class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Document
        fields = ['title', 'description']
