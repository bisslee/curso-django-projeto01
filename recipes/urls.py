from django.urls import path

from recipes.views import root

urlpatterns = [
    path('', root)
]
