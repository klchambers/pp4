from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe, IngredientQuantity
from .forms import CommentForm


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
