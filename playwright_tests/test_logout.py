from playwright.sync_api import Page
import pytest
from helpers import script_login, script_logout

def test_loginUser(page: Page):
    script_login(page)
    script_logout(page)
    try:
        # Verifica se botão logout aparece (indica login com sucesso)
        page.wait_for_selector('input[data-test="login-button"]', timeout=5000)
    except:
        pytest.fail("Logout não foi bem-sucedido.")