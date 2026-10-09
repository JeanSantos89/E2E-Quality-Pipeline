from playwright.sync_api import Page
import time, pytest

def script_login(page: Page):
    page.goto('https://www.saucedemo.com/')
    page.wait_for_selector('input[id="user-name"]').click() # Seleciona campo login
    page.wait_for_selector('input[id="user-name"]').type("standard_user") # Adiciona login
    page.wait_for_selector('input[id="password"]').type("secret_sauce") # Adiciona Senha
    page.wait_for_selector('input[data-test="login-button"]').click() # Clica em login

def script_logout(page: Page):
    page.wait_for_selector('button[id="react-burger-menu-btn"]').click() # Seleciona opções
    page.wait_for_selector('a[id="logout_sidebar_link"]').click() # Clica em Logout

def script_filtro(page: Page):
    dropdown = page.query_selector('select[data-test="product-sort-container"]')
    dropdown.select_option(label="Price (low to high)") # Seleciona opção dentro do filtro

def script_adicionar_itens_carrinho(page: Page):
    primeiro_item = page.query_selector('(//div[@class="inventory_list"]/div)[1]')  # Ve o primeiro item da lista
    primeiro_item.query_selector('button[id="add-to-cart-sauce-labs-backpack"]').click() # Adiciona ao carrinho o primeiro item
    ultimo_item = page.query_selector('(//div[@class="inventory_list"]/div)[last()]')   # Ve o último item da lista
    ultimo_item.query_selector('button[id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click() # Adiciona ao carrinho o segundo item

def script_checkout(page: Page):
    page.wait_for_selector('a[data-test="shopping-cart-link"]').click()
    numero_items = page.locator('[data-test="cart-list"] >> [data-test="inventory-item"]')
    count = numero_items.count()
    if count == 2:
        checkout_btn = page.wait_for_selector('button[id="checkout"]').click()
        print(count)
        pass
    else:
        pytest.fail("A quantidade de items não condiz.")