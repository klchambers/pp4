from .models import Comment, Recipe, IngredientQuantity
from django import forms
from django.forms import inlineformset_factory


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Form for creating or editing a recipe.

    Fields:
        title (str): The title of the recipe.
        featured_image (ImageField): The featured image for the recipe.
        instructions (str): The cooking instructions for the recipe.
        total_cook_time (DurationField): The total cooking time for the recipe.
        ingredients (str): Ingredients input as a comma-separated string.
        quantities (str): Quantities input as a comma-separated string.
    """
    ingredients = forms.CharField(
        label='Ingredients',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter ingredients separated by commas'}))
    quantities = forms.CharField(
        label='Quantities',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter quantities separated by commas'}))

    class Meta:
        model = Recipe
        fields = (
            'title',
            'featured_image',
            'instructions',
            'total_cook_time',
        )
        widgets = {
            'total_cook_time': forms.TextInput(
                attrs={'placeholder': 'HH:MM:SS'}),
        }


# Links IngredientQuantity instances to a Recipe instance.
# Adapted from the inline formset section of Django documentation
# Available here:
# https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/
RecipeFormSet = inlineformset_factory(
    Recipe,
    IngredientQuantity,
    fields=['ingredient', 'quantity'],
    can_delete=False,
    extra=1)
