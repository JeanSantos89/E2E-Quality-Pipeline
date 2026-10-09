from playwright.sync_api import Page
import pytest
from helpers import script_login, script_adicionar_itens_carrinho

def test_colocarCarrinho(page: Page):
    script_login(page)
    script_adicionar_itens_carrinho(page)

    badge = page.wait_for_selector('span[data-test="shopping-cart-badge"]')
    quantidade = badge.inner_text()
    if quantidade != "2":
        pytest.fail(f"Esperado 2 itens no carrinho, mas o badge mostra {quantidade}.")
