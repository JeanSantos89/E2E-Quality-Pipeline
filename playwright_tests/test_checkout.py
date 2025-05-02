from playwright.sync_api import Page
import pytest
from test_carrinho_compras import test_colocarCarrinho
from helpers import script_login, script_checkout

def test_checkout(page: Page):
    test_colocarCarrinho(page)
    script_checkout(page)
