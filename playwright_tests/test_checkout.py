from playwright.sync_api import Page
import pytest
from helpers import script_login, script_adicionar_itens_carrinho, script_checkout

def test_checkout(page: Page):
    script_login(page)
    script_adicionar_itens_carrinho(page)
    script_checkout(page)
