from django.contrib.auth.models import User
from django.db import models

class Dataset(models.Model):
    # Dataset Title
    title = models.CharField(max_length=100)

    # Beschreibung
    description = models.TextField()

    # Tags
    tags = models.CharField(max_length=100)

    # Dateigröße
    size = models.IntegerField(default=0)

    # Version
    version = models.FloatField(default=1.0)

    # Datei
    file = models.FileField(upload_to='datasets/', blank=True, null=True)  # Neues FileField

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # User who created or last modified the dataset
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_datasets')
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modifier_datasets')

    # Wird ausgegeben, sobald eine Klasseninstanz geprintet wird
    def __str__(self):
        return f"{self.title}({self.size}) - {self.description}..."
