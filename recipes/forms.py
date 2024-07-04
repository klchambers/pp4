from .models import Comment, Recipe, IngredientQuantity, Category
from django import forms
from django.forms import inlineformset_factory


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'recipe_category',
            'instructions',
            'total_cook_time',
        )
        widgets = {
            'total_cook_time': forms.TextInput(
                attrs={'placeholder': 'HH:MM:SS'}),
        }


# Adapted from the inline formset section of Django documentation
# Available here:
# https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/
RecipeFormSet = inlineformset_factory(
    Recipe, IngredientQuantity,
    fields=['ingredient', 'quantity'])
