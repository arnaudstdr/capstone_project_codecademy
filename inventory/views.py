from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Ingredient, MenuItem, RecipeRequirment, Purchase
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return render(request, 'inventory/index.html')

def add_item(request):
    return HttpResponse("Ajouter un nouvel élément à l'inventaire.")

# List View
class IngredientListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    context_object_name = 'ingredients'

class MenuItemListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = MenuItem
    template_name = 'inventory/menuitem_list.html'
    context_object_name = 'menuitem'

class RecipeRequirmentListView(LoginRequiredMixin, ListView):
    model = RecipeRequirment
    template_name = 'inventory/recipe_requierment.html'
    context_object_name = 'reciperequirment'    

class PurchaseListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Purchase
    template_name = 'inventory/purchase.html'
    context_object_name = 'purchases'

# Create View
class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_form.html'
    fields = ['name', 'quantity', 'unit', 'unit_price']
    success_url = reverse_lazy('ingredient-list')

class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = 'inventory/menuitem_form.html'
    fields = ['title', 'price']
    success_url = reverse_lazy('menuitem-list')

class RecipeRequirmentCreateView(LoginRequiredMixin, CreateView):
    model = RecipeRequirment
    template_name = 'inventory/reciperequirment_form.html'
    fields = ['menu_item', 'ingredient', 'quantity']
    success_url = reverse_lazy('reciperequirment-list')

class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = 'inventory/purchase_form.html'
    fields = ['menu_item']
    success_url = reverse_lazy('purchase-list')

# Update View
class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_form.html'
    fields = ['name', 'quantity', 'unit', 'unit_price']
    success_url = reverse_lazy('ingredient-list')

class MenuItemUpdateView(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = 'inventory/menuitem_form.html'
    fields = ['title', 'price']
    success_url = reverse_lazy('menuitem-list')

class RecipeRequirmentUpdateView(LoginRequiredMixin, UpdateView):
    model = RecipeRequirment
    template_name = 'inventory/reciperequirment_form.html'
    fields = ['menu_item', 'ingredient', 'quantity']
    success_url = reverse_lazy('reciperequirment-list')

class PurchaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = 'inventory/purchase_form.html'
    fields = ['menu_item', 'timestamp']
    success_url = reverse_lazy('purchase-list')

# Delete View
class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_confirm_delete.html'
    success_url = reverse_lazy('ingredient-list')

class MenuItemDeleteView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = 'inventory/menuitem_confirm_delete.html'
    success_url = reverse_lazy('menuitem-list')

class RecipeRequirmentDeleteView(LoginRequiredMixin, DeleteView):
    model = RecipeRequirment
    template_name = 'inventory/reciperequirment_confirm_delete.html'
    success_url = reverse_lazy('reciperequirment-list')

class PurchaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = 'inventory/purchase_confirm_delete.html'
    success_url = reverse_lazy('purchase-list')

# Total
class TotalsView(LoginRequiredMixin, View):
    login_url = 'login'  # Rediriger vers la page de connexion si non connecté
    def get(self, request, *args, **kwargs):
        # Calculer le revenu total
        purchases = Purchase.objects.all()
        total_revenue = sum(purchase.menu_item.price for purchase in purchases)
        
        # Calculer le coût total
        recipe_requirements = RecipeRequirment.objects.all()
        total_cost = sum(recipe.quantity * recipe.ingredient.unit_price for recipe in recipe_requirements)
        
        # Calculer le profit (revenu - coût)
        total_profit = total_revenue - total_cost
        
        # Passer les totaux au template
        return render(request, 'inventory/totals.html', {
            'total_revenue': total_revenue,
            'total_cost': total_cost,
            'total_profit': total_profit
        })