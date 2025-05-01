from playwright.sync_api import Page

def script_login(page: Page):
    page.goto('https://www.saucedemo.com/')
    page.wait_for_selector('input[id="user-name"]').click() # Seleciona campo login
    page.wait_for_selector('input[id="user-name"]').type("standard_user") # Adiciona login
    page.wait_for_selector('input[id="password"]').type("secret_sauce") # Adiciona Senha
    page.wait_for_selector('input[data-test="login-button"]').click() # Clica em login

def script_logout(page: Page):
    page.wait_for_selector('button[id="react-burger-menu-btn"]').click() # Seleciona opções
    page.wait_for_selector('a[id="logout_sidebar_link"]').click() # Clica em Logout
