from django import forms
from .models import Dataset


class DatasetForm(forms.ModelForm):

    class Meta:
        model = Dataset
        fields = ['title', 'description', 'tags', 'size', 'version', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.HiddenInput(),
            'size': forms.NumberInput(attrs={'class': 'form-control', 'label':'Size (in KB)', 'required':False}),
            'version': forms.NumberInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'creator': forms.Select(attrs={'class': 'form-control'}),
            'last_modified_by': forms.Select(attrs={'class': 'form-control'}),
        }
