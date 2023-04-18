
from django.shortcuts import render


# Create your views here.
def root(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Biss Lee',
        'greetins': 'Good night'
    })
