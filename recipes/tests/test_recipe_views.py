from django.urls import resolve, reverse

from recipes import views
from recipes.tests.test_recipe_base import RecipeTestBase

NO_RECIPE = 'Não tem receitas cadastradas ainda!'
RECIPES_HOME = 'recipes:home'
RECIPES_CATEGORY = 'recipes:category'
RECIPES_RECIPE = 'recipes:recipe'


class RecipeViewsTest(RecipeTestBase):

    # Test
    def test_aprendendo_assert_Is(self):
        lista_a = ['aa', 'bb', 'cc']
        lista_b = lista_a
        self.assertIs(lista_a, lista_b)

    # Home

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

    def test_recipe_home_template_loads_recipes(self):
        recipe = self.make_recipe()
        servings_all = f'{recipe.servings} {recipe.servings_unit}'
        prep_unit = recipe.preparation_time_unit
        prepation_all = f'{recipe.preparation_time} {prep_unit}'

        response = self.client.get(reverse(RECIPES_HOME))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertEqual(
            response_context_recipes.first().title, recipe.title)
        self.assertIn(recipe.title, content)
        self.assertIn(servings_all, content)
        self.assertIn(prepation_all, content)
        self.assertEqual(len(response_context_recipes), 1)

    # Category

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse(RECIPES_CATEGORY, kwargs={'category_id': 1}))
        self.assertIs(view.func, views.categories)

    def test_recipe_category_view_returns_404_if_no_recipes(self):
        response = self.client.get(
            reverse(RECIPES_CATEGORY, kwargs={'category_id': 23}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        recipe = self.make_recipe()

        response = self.client.get(
            reverse(RECIPES_CATEGORY, kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn(recipe.category.name, content)
        self.assertEqual(len(response_context_recipes), 1)

    # Detail

    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse(RECIPES_RECIPE, kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes(self):
        response = self.client.get(
            reverse(RECIPES_RECIPE, kwargs={'id': 23}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_correct_recipe(self):
        recipe = self.make_recipe(
            title='Esse é uma receita de Detalhe'
        )

        response = self.client.get(reverse(RECIPES_RECIPE, kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(recipe.title, content)
