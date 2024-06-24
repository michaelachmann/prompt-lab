from django import forms
from .models import Dataset

class DatasetForm(forms.ModelForm):
    file = forms.FileField(required=False)  # Datei-Feld, das nicht im Modell gespeichert wird
    size = forms.CharField(label='Size (in KB)', required=False)  # Hier wird das Label gesetzt

    class Meta:
        model = Dataset
        fields = ['title', 'description', 'tags', 'size', 'version', 'file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget = forms.HiddenInput()  # Verstecke das Tags-Feld
