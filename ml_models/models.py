from django.db import models

# Create your models here.
class MLModel(models.Model):

    # Model name
    name = models.CharField(max_length=100)

    # Model type
    type = models.CharField(max_length=100)

    # Description
    description = models.TextField()

    # Tags
    tags = models.CharField(max_length=100)

    # Parameter count
    parameters = models.IntegerField()

    # Model size (in GB)
    size = models.IntegerField()

    # Model version
    version = models.FloatField(default=1.0)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

