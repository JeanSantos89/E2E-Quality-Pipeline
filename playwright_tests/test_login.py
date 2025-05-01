from playwright.sync_api import Page
import pytest
from helpers import script_login

def test_fazerLogin(page: Page):
    script_login(page)
    try:
        page.wait_for_selector('input[data-test="login-button"]', state='detached', timeout=2000)
    except:
        pytest.fail("Login não foi bem-sucedido. Botão de login ainda está presente na tela após o timeout")
