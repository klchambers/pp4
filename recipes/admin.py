from django.contrib import admin
from .models import Recipe, Category, Ingredient, IngredientQuantity, Comment # noqa
from django_summernote.admin import SummernoteModelAdmin


class IngredientQuantityInline(admin.TabularInline):
    model = IngredientQuantity


class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_by')
    search_fields = ('category_name',)


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    inlines = [IngredientQuantityInline,]
    list_display = ('title', 'author', 'created_on', 'status')
    search_fields = ('title', 'author__username')
    list_filter = ('status', 'created_on', 'recipe_category')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('recipe_category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Comment)
