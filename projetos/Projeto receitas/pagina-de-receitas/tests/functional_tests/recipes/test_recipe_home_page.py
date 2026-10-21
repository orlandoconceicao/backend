from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import RecipeBaseFunctionalTest
from unittest.mock import patch
import pytest


@pytest.mark.functional_test # pytest -m 'functional_test' > apenas o selecionado
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    def test_recipe_home_page_without_recipes_not_fould_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Nenhuma receita encontrada', body.text)
        
    
    @patch('recipes.views.PER_PAGE', new=3)
    def test_recipe_search_input_can_find_correct_recipes(self):
        recipes = self.make_recipe_in_batch()
        # usuário abre a página
        self.browser.get(self.live_server_url)
        # ve um campo de busca com o texto "Pesquisar receita..."
        search_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Pesquisar receita..."]')
        # clica neste input e digita o termo "Recipe title 1" para encontrar a receita
        search_input.send_keys(recipes[0].title)
        search_input.send_keys(Keys.ENTER)
        
