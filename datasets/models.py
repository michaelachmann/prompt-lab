from django.contrib.auth.models import User
from django.db import models

# Create your datasets here.
from django.db import models

class Dataset(models.Model):
    # Dataset Title
    title = models.CharField(max_length=100)

    #Beschreibung
    description = models.TextField()

    #Tags
    tags = models.CharField(max_length=100)


    #Dateigröße
    size = models.IntegerField()

    #Version
    version = models.FloatField(default=1.0)


    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # User who created or last modified the prompt
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_datasets')
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modifier_datasets')

# Create your models here.

def __str__(self):
    return f"{self.title}({self.size}) - {self.description}..."
