from django.urls import path
from .views import IngredientListView, IngredientCreateView, IngredientUpdateView, IngredientDeleteView, MenuItemListView, MenuItemCreateView, MenuItemUpdateView, MenuItemDeleteView, RecipeRequirmentListView, RecipeRequirmentCreateView, RecipeRequirmentUpdateView, RecipeRequirmentDeleteView, PurchaseListView, PurchaseCreateView, PurchaseUpdateView, PurchaseDeleteView, TotalsView     # Importer les vues que je crééerais
from . import views

urlpatterns = [
    # path('', views.index, name='index'),      # Route pour la page d'acceuil de l'application
    path('ingredients/', IngredientListView.as_view(), name='ingredient-list'),
    path('ingredients/new/', IngredientCreateView.as_view(), name="ingredient-create"),
    path('ingredients/<int:pk>/edit/', IngredientUpdateView.as_view(),name='ingredient-update'),
    path('ingredients/<int:pk>/delete/', IngredientDeleteView.as_view(), name='ingredient-delete'),
    path('menuitem/', MenuItemListView.as_view(), name='menuitem-list'),
    path('menuitem/new/', MenuItemCreateView.as_view(), name="menuitem-create"),
    path('menuitem/<int:pk>/edit/', MenuItemUpdateView.as_view(),name='menuitem-update'),
    path('menuitem/<int:pk>/delete/', MenuItemDeleteView.as_view(), name='menuitem-delete'),
    path('reciperequirment/', RecipeRequirmentListView.as_view(), name='reciperequirment-list'),
    path('reciperequirment/new/', RecipeRequirmentCreateView.as_view(), name="reciperequirment-create"),
    path('reciperequirment/<int:pk>/edit/', RecipeRequirmentUpdateView.as_view(),name='reciperequirment-update'),
    path('reciperequirment/<int:pk>/delete/', RecipeRequirmentDeleteView.as_view(), name='reciperequirment-delete'),
    path('purchase/', PurchaseListView.as_view(), name='purchase-list'),
    path('purchase/new/', PurchaseCreateView.as_view(), name="purchase-create"),
    path('purchase/<int:pk>/edit/', PurchaseUpdateView.as_view(),name='purchase-update'),
    path('purchase/<int:pk>/delete/', PurchaseDeleteView.as_view(), name='purchase-delete'),
    path('totals/', TotalsView.as_view(), name='totals'),
]