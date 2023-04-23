from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

NO_RECIPE = 'Não tem receitas cadastradas ainda!'
RECIPES_HOME = 'recipes:home'
RECIPES_CATEGORY = 'recipes:category'
RECIPES_RECIPE = 'recipes:recipe'


class RecipeViewsTest(TestCase):
    def test_aprendendo_assert_Is(self):
        lista_a = ['aa', 'bb', 'cc']
        lista_b = lista_a
        self.assertIs(lista_a, lista_b)

    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse(RECIPES_HOME))
        self.assertIs(view.func, views.root)

    def test_recipe_home_view_returns_status_code_200_0k(self):
        response = self.client.get(reverse(RECIPES_HOME))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_load_correct_template(self):
        response = self.client.get(reverse(RECIPES_HOME))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse(RECIPES_HOME))
        self.assertIn(NO_RECIPE, response.content.decode('utf-8'))

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse(RECIPES_CATEGORY, kwargs={'category_id': 1}))
        self.assertIs(view.func, views.categories)

    def test_recipe_category_view_returns_404_if_no_recipes(self):
        response = self.client.get(
            reverse(RECIPES_CATEGORY, kwargs={'category_id': 23}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse(RECIPES_RECIPE, kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes(self):
        response = self.client.get(
            reverse(RECIPES_RECIPE, kwargs={'id': 23}))
        self.assertEqual(response.status_code, 404)
