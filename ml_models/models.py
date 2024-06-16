from django.db import models

# Create your models here.
class MLModel(models.Model):
    # Let's define the options for the rating
    RATING_CHOICES = [
        (1, 'Poor'),
        (2, 'Fair'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    ]

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

    # Ratings: Users can select one of the options above
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=3)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

