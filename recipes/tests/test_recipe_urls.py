
from django.test import TestCase
from django.urls import reverse

RECIPES_HOME = 'recipes:home'
RECIPES_CATEGORY = 'recipes:category'
RECIPES_RECIPE = 'recipes:recipe'


class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1

    def test_recipe_home_url_is_correct(self):
        url = reverse(RECIPES_HOME)
        self.assertEqual(url, '/')

    def test_category_url_is_correct(self):
        url = reverse(RECIPES_CATEGORY, kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_url_is_correct(self):
        url = reverse(RECIPES_RECIPE, kwargs={'id': 5})
        self.assertEqual(url, '/recipes/5/')
