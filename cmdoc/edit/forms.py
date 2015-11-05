from django import forms
from edit import models

class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Document
        fields = ['title', 'description']


class SectionForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = ['content', 'position', 'message']
