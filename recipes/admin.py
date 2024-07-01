from django.contrib import admin
from .models import Recipe, Category, Ingredient, RecipeIngredient # noqa


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_by')
    search_fields = ('category_name',)


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]
    list_display = ('title', 'author', 'created_on', 'status')
    search_fields = ('title', 'author__username')
    list_filter = ('status', 'created_on', 'recipe_category')
    # filter_horizontal = ('ingredients',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
