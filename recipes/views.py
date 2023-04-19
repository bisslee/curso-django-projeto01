
from django.shortcuts import render

from utils.factory import make_recipe


# Create your views here.
def root(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Biss Lee',
        'greetins': 'Good night',
        'recipes': [make_recipe() for _ in range(11)]
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html', context={
        'name': 'Biss Lee',
        'greetins': 'Good night',
        'recipe': make_recipe(),
        'id': id
    })
