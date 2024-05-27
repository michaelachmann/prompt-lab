from django import forms
from .models import Dataset


class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['title', 'description', 'tags', 'size', 'version']  # Fügen Sie weitere Felder nach Bedarf hinzu
