from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('upload_recipe/', views.upload_recipe, name='upload_recipe'),
    path('<slug:slug>/', views.recipe_page, name='recipe_page'),
]
