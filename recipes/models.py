from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Category(models.Model):
    # category name limit of 50 characters & must be unique prevent duplicates
    category_name = models.CharField(max_length=50, unique=True)
    """
    Foreign Key, one user can create many recipe categories
    and SET_NULL ensures categories retained even if a user account is deleted
    """
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_recipes")
    recipe_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="category_posts",
        null=True)
    ingredients = models.TextField(null=True)
    instructions = models.TextField(null=True)
    total_cook_time = models.DurationField(
        null=True,
        blank=True,
        default=None,
        # help_text displays formatting instructions to the user
        help_text='Please enter the total cook time in the format HH:MM (e.g., 01:30 for 1 hour and 30 minutes).') # noqa
    created_on = models.DateTimeField(auto_now_add=True)
    # default=0 sets default status of a new post to 'draft' not 'published'
    status = models.IntegerField(choices=STATUS, default=0)
