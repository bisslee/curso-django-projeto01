from django.urls import path

from recipes.views import about, contact, root

urlpatterns = [
    path('sobre/', about),
    path('contato/', contact),
    path('', root)
]
