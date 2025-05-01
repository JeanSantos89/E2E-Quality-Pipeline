from playwright.sync_api import Page
import pytest
from helpers import script_login, script_filtro

def test_filtro(page: Page):
    script_login(page)
    script_filtro(page)
    primeiro_item = page.query_selector('(//div[@class="inventory_list"]/div)[1]')  # Ve o primeiro item da lista
    preco1 = primeiro_item.query_selector('.inventory_item_price').inner_text() # Recebe o preço do primeiro item da lista

    ultimo_item = page.query_selector('(//div[@class="inventory_list"]/div)[last()]')   # Seleciona o último item da lista
    preco2 = ultimo_item.query_selector('.inventory_item_price').inner_text() # Recebe o preço do ultimo item da lista

    preco1 = float(preco1.strip('$').replace(',', ''))  # Remove símbolos e converte para float
    preco2 = float(preco2.strip('$').replace(',', ''))  # Remove símbolos e converte para float

    print(f"Preco1: {preco1}")
    print(f"Preco2: {preco2}")
    
    if(preco2>preco1):
        print(preco2)
        print(preco1)
        pass
    else:
        pytest.fail("Filtro foi aplicado errado.")
        
