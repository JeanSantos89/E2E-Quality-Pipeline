from playwright.sync_api import Page
import pytest
from helpers import script_login

def test_descricao_produtos(page: Page):
    script_login(page)

    primeiro_item = page.query_selector('(//div[@class="inventory_list"]/div)[1]')  # Ve o primeiro item da lista
    descricao_produto = primeiro_item.query_selector('.inventory_item_desc').inner_text() # Recebe a descrição do primeiro item da lista

    if len(descricao_produto) > 0: # Se o tamanho da descrição for maior que 0
        print("Teste passou: descrição encontrada.")
    else:
        raise Exception("Teste falhou: descrição vazia.")


