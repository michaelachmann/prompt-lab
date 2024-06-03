from django.contrib.auth.models import User
from django.db import models
from datasets.models import Dataset
from ml_model.models import MLModel
from prompts.models import Prompt


# Create your models here.
class Experiment(models.Model):
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
    description = models.TextField()

    # Machine Learning Metrics
    f1_score_macro = models.FloatField(null=True, blank=True)
    f1_score_micro = models.FloatField(null=True, blank=True)
    f1_score_weighted = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    recall = models.FloatField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)

    # Additional notes
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_experiments')
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_experiments')

    def __str__(self):
        return f"Experiment with {self.model.name} on {self.dataset.title} using {self.prompt.title}"
