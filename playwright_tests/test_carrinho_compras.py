from playwright.sync_api import Page
import pytest
from helpers import script_login

def test_colocarCarrinho(page: Page):
    script_login(page)
    primeiro_item = page.query_selector('(//div[@class="inventory_list"]/div)[1]')  # Ve o primeiro item da lista
    add_cart1 = primeiro_item.query_selector('button[id="add-to-cart-sauce-labs-backpack"]').click() # Adiciona ao carrinho o primeiro item
    ultimo_item = page.query_selector('(//div[@class="inventory_list"]/div)[last()]')   # Ve o último item da lista
    add_cart2 = ultimo_item.query_selector('button[id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click() # Adiciona ao carrinho o segundo item
    