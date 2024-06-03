from django import forms
from .models import Prompt

class MLmodelForm(forms.ModelForm):
    class Meta:
        model = MLmodel
        fields = ['name', 'type', 'description', 'tags', 'parameters', 'size', 'version']  # Fügen Sie weitere Felder nach Bedarf hinzu