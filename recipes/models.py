from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    # category name limit of 50 characters & must be unique prevent duplicates
    category_name = models.CharField(max_length=50, unique=True)
    """
    Foreign Key, one user can create many recipe categories
    and SET_NULL ensures categories retained even if a user account is deleted
    """
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.category_name


class Ingredient(models.Model):
    """
    Ingredient model has many-to-many relationship with Recipe model
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Ingredient Name')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Recipe model represents a recipe entry in the application
    """
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_recipes")
    featured_image = CloudinaryField('image', default='placeholder')
    recipe_category = models.ManyToManyField(
        Category,
        related_name="category_recipes",
        blank=True)
    instructions = models.TextField(null=True,
                                    help_text='''Please enter each new step on
    a new line preceded by a hyphen (-) or number (e.g. 1:..., 2:...)).''')
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
        help_text='Please enter the total cook time in the format HH:MM:SS (e.g., 01:30:00 for 1 hour and 30 minutes).') # noqa
    created_on = models.DateTimeField(auto_now_add=True)
    # default=0 sets default status of a new post to 'draft' not 'published'
    status = models.IntegerField(choices=STATUS, default=0)

    # Use of slugify adapted from code posted by Ikechukwu Henry Odoh
    # In this Stack Overflow thread:
    # https://stackoverflow.com/questions/50436658/how-to-auto-generate-slug-from-my-album-model-in-django-2-0-4
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    class meta():
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | posted by {self.author} on {self.created_on}"

    @property
    def comment_count(self):
        return self.comments.filter(approved=True).count()


class IngredientQuantity(models.Model):
    """
    IngredientQuantity link a quantity value to
    an ingredient in a specific recipe
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"""
    {self.quantity} of {self.ingredient.name} in {self.recipe.title}"""


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
