from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe, IngredientQuantity
from .forms import CommentForm, RecipeFormSet, RecipeForm
from django.contrib.auth.decorators import login_required


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
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
            recipe = form.save(commit=False)
            formset = RecipeFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                # Save recipe form data once valid
                recipe.save()
                # save ingredient formset
                formset.save()
                # redirect to homepage
                return redirect('home')
        else:
            formset = RecipeFormSet(request.POST, instance=recipe)
    else:
        form = RecipeForm(instance=recipe)
        formset = RecipeFormSet(instance=recipe)

    return render(
        request, 'recipes/upload_recipe.html',
        {'formset': formset, 'form': form})
