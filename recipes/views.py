from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse)
from django.views import generic
from .models import (
    Recipe,
    Ingredient,
    IngredientQuantity,
    Comment)
from .forms import CommentForm, RecipeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


class RecipeList(generic.ListView):
    """
    View to list all published recipes, ordered by creation date.
    """
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = "recipes/index.html"
    paginate_by = 6


def recipe_page(request, slug):
    """
    Display an individual recipe along with its ingredients,
    quantities, and comments.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Recipe`.
    ``ingredient_quantities``
        A list of instances of :model:`recipe.IngredientQuantity`
        for the recipe.
    ``comments``
        A list of instances of :model:`recipe.Comment` for the recipe.
    ``comment_count``
        The number of approved comments for the recipe.
    ``comment_form``
        An instance of :form:`recipe.CommentForm` for adding new comments.

    **Template:**

    :template:`recipes/recipe_page.html`
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
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

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


# login required decorator docs:
# https://docs.djangoproject.com/en/5.0/topics/auth/default/#auth-admin
@login_required
def upload_recipe(request, recipe_id=None):
    """
    Handle uploading a new recipe.

    **Context**

    ``form``
        An instance of :form:`recipe.RecipeForm` for submitting recipe data.

    **Template:**

    :template:`recipes/upload_recipe.html`
    """
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            # Save the recipe
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your recipe is submitted and awaiting approval!'
            )
            # Process ingredients and quantities
            ingredients_input = form.cleaned_data['ingredients']
            quantities_input = form.cleaned_data['quantities']

            ingredients_list = [ingredient.strip().capitalize()
                                for ingredient in ingredients_input.split(',')
                                if ingredient.strip()]
            quantities_list = [quantity.strip()
                               for quantity in quantities_input.split(',')
                               if quantity.strip()]

            # Create IngredientQuantity instances
            for idx, ingredient_name in enumerate(ingredients_list):
                ingredient, _ = Ingredient.objects.get_or_create(
                    name=ingredient_name)

                # Create IngredientQuantity instance
                IngredientQuantity.objects.create(
                    recipe=recipe,
                    ingredient=ingredient,
                    quantity=quantities_list[idx] if idx < len(quantities_list)
                    else ''
                )
            # Redirect after successful save
            return redirect('home')
    else:
        form = RecipeForm()

    return render(request, 'recipes/upload_recipe.html', {'form': form})


def comment_edit(request, slug, comment_id):
    """
    View to edit an existing comment on a recipe.

    **Context**

    None.

    **Redirect:**

    Redirects to the recipe page after the comment is edited.
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_page', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug) # noqa
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_page', args=[slug]))


@login_required
def delete_recipe(request, slug):
    """
    Handle the deletion of a recipe by its author.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Recipe`.

    **Template:**

    :template:`recipes/delete_recipe.html`
    """
    recipe = get_object_or_404(Recipe, slug=slug)

    # Check if the logged-in user is the author of the recipe
    if recipe.author != request.user:
        return redirect('recipe_page', slug=recipe.slug)

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully!')
        return redirect('home')  # Redirect to recipe_page

    # If the request method is not POST, render the confirmation template
    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})
