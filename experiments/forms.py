from django import forms
from .models import Experiment

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['prompt', 'dataset', 'model', 'description', 'f1_score_macro', 'f1_score_micro', 'f1_score_weighted', 'precision', 'recall', 'accuracy', 'notes']
        widgets = {
            'prompt': forms.Select(attrs={'class': 'form-control'}),
            'dataset': forms.Select(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'f1_score_macro': forms.NumberInput(attrs={'class': 'form-control'}),
            'f1_score_micro': forms.NumberInput(attrs={'class': 'form-control'}),
            'f1_score_weighted': forms.NumberInput(attrs={'class': 'form-control'}),
            'precision': forms.NumberInput(attrs={'class': 'form-control'}),
            'recall': forms.NumberInput(attrs={'class': 'form-control'}),
            'accuracy': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }