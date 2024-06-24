from django import forms
from .models import MLModel


class MLModelForm(forms.ModelForm):
    class Meta:
        model = MLModel
        fields = ['name', 'type', 'description', 'tags', 'parameters', 'size', 'version',
                  'rating']  # Fügen Sie weitere Felder nach Bedarf hinzu
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'parameters': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.NumberInput(attrs={'class': 'form-control'}),
            'version': forms.NumberInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
