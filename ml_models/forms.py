from django import forms
from .models import MLModel

class MLModelForm(forms.ModelForm):
    class Meta:
        model = MLModel
        fields = ['name', 'type', 'description', 'tags', 'parameters', 'size', 'version']  # Fügen Sie weitere Felder nach Bedarf hinzu