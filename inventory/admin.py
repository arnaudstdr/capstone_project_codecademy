from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirment, Purchase

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirment)
admin.site.register(Purchase)
