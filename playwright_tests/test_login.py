from playwright.sync_api import Page
import pytest

def test_loginUser(page: Page):
    page.goto('https://www.saucedemo.com/')
    page.wait_for_selector('input[id="user-name"]').click() # Seleciona campo login
    page.wait_for_selector('input[id="user-name"]').type("standard_user") # Adiciona login
    page.wait_for_selector('input[id="password"]').type("secret_sauce") # Adiciona Senha
    page.wait_for_selector('input[data-test="login-button"]').click() # Clica em login

    try:
        page.wait_for_selector('input[data-test="login-button"]', state='detached', timeout=2000)
    except:
        pytest.fail("Login não foi bem-sucedido. Botão de login ainda está presente na tela após o timeout")
