
from django.shortcuts import render


# Create your views here.
def root(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Biss Lee',
        'greetins': 'Good night'
    })


def recipe(request, id):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Biss Lee',
        'greetins': 'Good night',
        'id': id
    })
