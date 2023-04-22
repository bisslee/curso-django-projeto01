
from django.shortcuts import get_list_or_404, get_object_or_404, render

from utils.factory import make_recipe

from .models import Recipe


def root(request):
    recipes = Recipe.objects.filter(is_publish=True).order_by('title')
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Biss Lee',
        'greetins': 'Good night',
        'recipes': recipes,
        'is_detail_page': False
    })


def categories(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id, is_publish=True).order_by('title'))

    category_name = recipes[0].category.name
    return render(request, 'recipes/pages/category.html', context={
        'name': 'Biss Lee',
        'greetins': 'Good night',
        'recipes': recipes,
        'is_detail_page': False,
        'category_name': category_name
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_publish=True)
    return render(request, 'recipes/pages/recipe.html', context={
        'name': 'Biss Lee',
        'greetins': 'Good night',
        'recipe': recipe,
        'id': id,
        'is_detail_page': True
    })
