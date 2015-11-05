from django import forms
from edit import models

class SectionForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = ['content', 'position', 'message']
