from playwright.sync_api import Page
import pytest
from test_carrinho_compras import test_colocarCarrinho
from helpers import script_login

def test_checkout(page: Page):
    test_colocarCarrinho(page)
    page.wait_for_selector('a[data-test="shopping-cart-link"]').click()
    numero_items = page.locator('[data-test="cart-list"] >> [data-test="inventory-item"]')
    count = numero_items.count()
    if count == 2:
        checkout_btn = page.wait_for_selector('button[id="checkout"]').click()
        print(count)
        pass
    else:
        pytest.fail("A quantidade de items não condiz.")
