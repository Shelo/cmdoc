from django import forms
from tokens import models

class TokenForm(forms.ModelForm):
    class Meta:
        model = models.Token
        fields = ['key', 'value']
