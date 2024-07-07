from .models import Comment, Recipe, IngredientQuantity
from django import forms
from django.forms import inlineformset_factory


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):

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


# Adapted from the inline formset section of Django documentation
# Available here:
# https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/
RecipeFormSet = inlineformset_factory(
    Recipe,
    IngredientQuantity,
    fields=['ingredient', 'quantity'],
    can_delete=False,
    extra=1)
