from django.contrib.auth.models import User
from django.test import TestCase

from recipes.models import Category, Recipe


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(self,
                    first_name='user',
                    last_name='last_user',
                    username='user_name',
                    email='user@email.com',
                    password='12345'):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )

    def make_recipe(self,
                    category_data=None,
                    author_data=None,
                    title='Titulo da Receita',
                    description='Descrição da Receita',
                    slug='titulo_da_receita',
                    preparation_time=30,
                    preparation_time_unit='Minutos',
                    servings='20',
                    servings_unit='pedaços',
                    preparation_steps='mode de preparo',
                    preparation_steps_is_html=False,
                    is_publish=True):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_publish=is_publish
        )
