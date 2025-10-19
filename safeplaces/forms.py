from django import forms
from .models import SafePlace

class SafePlaceForm(forms.ModelForm):
    class Meta:
        model = SafePlace
        fields = ['address', 'comment']
