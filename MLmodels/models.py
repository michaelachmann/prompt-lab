from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User


class MLmodel(models.Model):
    # Let's define the options for the rating
    RATING_CHOICES = [
        (1, 'Poor'),
        (2, 'Fair'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    ]

    # Model name
    title = models.CharField(max_length=100)

    # Basic prompt text
    text = models.TextField()

    # Categorization of prompts by type (e.g., education, health)
    category = models.CharField(max_length=100)

    # Ratings: Users can select one of the options above
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=3)

    # Version control to track changes - this is a simple implementation.
    # In practice, you might want to use a more robust approach like integrating with a version control system.
    version = models.IntegerField(default=1)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # User who created or last modified the prompt
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_prompts')
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_prompts')


    def __str__(self):
        return f"{self.title} - {self.category}..."