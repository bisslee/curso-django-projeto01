from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.root, name='home'),
    path('recipes/category/<int:category_id>/',
         views.categories,  name='category'),
    path('recipes/<int:id>/',
         views.recipe,  name='recipe'),
]
