# Generated by Django 4.2.13 on 2024-07-01 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_remove_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeIngredient',
            new_name='IngredientQuantity',
        ),
    ]