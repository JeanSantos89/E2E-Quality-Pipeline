from playwright.sync_api import Page
import pytest
from helpers import script_login, script_adicionar_itens_carrinho

def test_colocarCarrinho(page: Page):
    script_login(page)
    script_adicionar_itens_carrinho(page)
    