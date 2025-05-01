from playwright.sync_api import Page
import pytest
from helpers import script_login, script_filtro

def test_filtro(page: Page):
    script_login(page)
    script_filtro(page)
    primeiro_item = page.wait_for_selector('(//div[@class="inventory_list"]/div)[1]')  # Ve o primeiro item da lista
    preco1 = primeiro_item.query_selector('.inventory_item_price').inner_text() # Recebe o preço do primeiro item da lista

    ultimo_item = page.wait_for_selector('(//div[@class="invetory_list"]/div)[last()')   # Seleciona o ultimo item da lista
    preco2 = ultimo_item.query_selector('.inventory_item_price').inner_text() # Recebe o preço do ultimo item da lista

    if(preco2>preco1):
        print(preco2)
        print(preco1)
        pass
    else:
        pytest.fail("Filtro foi aplicado errado.")
        
