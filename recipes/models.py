from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    # category name limit of 50 characters & must be unique prevent duplicates
    category_name = models.CharField(max_length=50, unique=True)
    """
    Foreign Key, one user can create many recipe categories
    and SET_NULL ensures categories retained even if a user account is deleted
    """
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Ingredient(models.Model):
    """
    Ingredient model has many-to-many relationship with Recipe model
    """
    name = models.CharField(
        max_length=100, unique=True, verbose_name='Ingredient Name')
    quantity = models.CharField(
        max_length=50, verbose_name='Ingredient Quantity')


class Recipe(models.Model):
    """
    Recipe model represents a recipe entry in the application
    """
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_recipes")
    recipe_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="category_recipes",
        null=True)
    ingredients = models.ManyToManyField(
        Ingredient,
    )
    instructions = models.TextField(null=True)
    """
    DurationField = 'A field for storing periods of time - modeled in Python
    by timedelta.'
    - https://docs.djangoproject.com/en/1.10/ref/models/fields/#durationfield
    """
    total_cook_time = models.DurationField(
        null=True,
        blank=True,
        default=None,
        # help_text displays formatting instructions to the user
        help_text='Please enter the total cook time in the format HH:MM (e.g., 01:30 for 1 hour and 30 minutes).') # noqa
    created_on = models.DateTimeField(auto_now_add=True)
    # default=0 sets default status of a new post to 'draft' not 'published'
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.title} | posted by {self.author} on {self.created_on}"
