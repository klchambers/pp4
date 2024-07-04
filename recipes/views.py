from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe, Ingredient, IngredientQuantity
from .forms import CommentForm, RecipeForm
from django.contrib.auth.decorators import login_required


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = "recipes/index.html"
    paginate_by = 6


def recipe_page(request, slug):
    """
    Display an individual :model:`recipe.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Recipe`.

    **Template:**

    :template:`recipe/recipe_page.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    ingredient_quantities = IngredientQuantity.objects.filter(recipe=recipe)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()

    comment_form = CommentForm()

    context = {
        'recipe': recipe,
        'ingredient_quantities': ingredient_quantities,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form}

    return render(
        request,
        "recipes/recipe_page.html",
        context,
    )


# def upload_recipe(request):
#     if request.method == 'POST':
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             recipe = form.save(commit=False)
#             recipe.author = request.user
#             recipe.save()
#             form.save_m2m()  # Save the many-to-many data for the form
#             # Redirect sto recipe_page
#             return redirect('recipe_page', slug=recipe.slug)
#     else:
#         form = RecipeForm()

#     return render(request, 'recipes/upload_recipe.html', {'form': form})


# login required decorator docs:
# https://docs.djangoproject.com/en/5.0/topics/auth/default/#auth-admin
@login_required
def upload_recipe(request, recipe_id=None):
    if recipe_id:
        recipe = get_object_or_404(Recipe, id=recipe_id)
    else:
        recipe = Recipe(author=request.user)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            # Save the recipe
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            # Extract ingredients and quantities
            ingredients_input = form.cleaned_data['ingredients']
            quantities_input = form.cleaned_data['quantities']

            ingredients_list = [ingredient.strip().capitalize()
                                for ingredient in ingredients_input.split(',')
                                if ingredient.strip()]
            quantities_list = [quantity.strip()
                               for quantity in quantities_input.split(',')
                               if quantity.strip()]

            # Clear existing ingredient quantities for this recipe
            recipe.ingredients.clear()

            # Process ingredients and quantities
            for idx, ingredient_name in enumerate(ingredients_list):
                # Check if ingredient exists, otherwise create it
                ingredient, created = Ingredient.objects.get_or_create(
                    name=ingredient_name)

                # Create IngredientQuantity instance
                IngredientQuantity.objects.create(
                    recipe=recipe,
                    ingredient=ingredient,
                    quantity=quantities_list[idx] if idx < len(quantities_list)
                    else ''
                )
            # Redirect after successful recipe submission
            return redirect('recipe_page', slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/upload_recipe.html', {'form': form})
