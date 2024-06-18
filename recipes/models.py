from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_recipes")
    ingredients = models.TextField()
    instructions = models.TextField()
    total_cook_time = models.DurationField(
        help_text='Please enter the total cook time in the format HH:MM (e.g., 01:30 for 1 hour and 30 minutes).') # noqa
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
