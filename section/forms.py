from django import forms
from section import models

class SectionForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = ['content', 'position', 'message']
