from django.urls import path
from . import views

urlpatterns = [
     path('', views.RecipeList.as_view(), name='home'),
     path('upload_recipe/', views.upload_recipe, name='upload_recipe'),
     path('<slug:slug>/', views.recipe_page, name='recipe_page'),
     path('<slug:slug>/edit_comment/<int:comment_id>',
          views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
          views.comment_delete, name='comment_delete'),
     path('delete/<slug:slug>/', views.delete_recipe, name='delete_recipe'),
]
