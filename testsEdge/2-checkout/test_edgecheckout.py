import pytest
import time
from commands.autenticacao import *
from selenium.webdriver.common.by import By
from commands.login_helpers import loginEdge

@pytest.fixture
def log_in():
    driver = loginEdge(username, password)  
    yield driver
    driver.quit()

def test_checkout(log_in):
    cartBackpack = log_in.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']")
    cartBackpack.click()
    time.sleep(1)
    print('Produto 1 selecionado com Sucesso!')
    car = log_in.find_element(By.XPATH, "//*[@fill='currentColor']")
    car.click()
    print('btn Carrinho Clicado com Sucesso!')
    log_in.get_screenshot_as_file("testsEdge/2-checkout/report/checkout1.png")
    time.sleep(1)
    check = log_in.find_element(By.XPATH, "//*[@class='btn_action checkout_button']")
    check.click()
    print('btn checkout clicado com Sucesso!')
    firstName = log_in.find_element(By.XPATH, "//*[@id='first-name']")
    firstName.send_keys('joão')
    print('Nome inserido no formulário de checkout com Sucesso!')
    lasttName = log_in.find_element(By.XPATH, "//*[@id='last-name']")
    lasttName.send_keys('Da Silva')
    print('Sobrenome inserido no formulário de checkout com Sucesso!')
    post = log_in.find_element(By.XPATH, "//*[@id='postal-code']")
    post.send_keys('31.710.520')
    print('Cep inserido no formulário de checkout com Sucesso!')
    btnContinue = log_in.find_element(By.XPATH, "//*[@class='btn_primary cart_button']")
    btnContinue.click()
    print('btn Continue clicado com Sucesso!')
    price_div = log_in.find_element(By.XPATH, "//*[@class='inventory_item_price']")
    assert price_div.text == "$29.99", "O preço esperado não foi encontrado ou é diferente de $29.99"
    print('Valor assert confirmado com Sucesso!')
    price_div = log_in.find_element(By.XPATH, "//*[@class='summary_subtotal_label']")
    assert price_div.text == "Item total: $29.99", "O preço esperado não foi encontrado ou é diferente de $29.99"
    print('Valor assert confirmado com Sucesso!')
    price_div = log_in.find_element(By.XPATH, "//*[@class='summary_tax_label']")
    assert price_div.text == "Tax: $2.40", "A taxa esperada não foi encontrada ou é diferente de $2.40"
    print('Taxa assert confirmado com Sucesso!')
    price_div = log_in.find_element(By.XPATH, "//*[@class='summary_total_label']")
    assert price_div.text == "Total: $32.39", "O preço esperado não foi encontrado ou é diferente de $32.39"
    print('Valor total assert confirmado com Sucesso!')
    time.sleep(1)
    log_in.get_screenshot_as_file("testsEdge/2-checkout/report/checkout2.png")
    finish = log_in.find_element(By.XPATH, "//*[@class='btn_action cart_button']")
    finish.click()
    log_in.get_screenshot_as_file("testsEdge/2-checkout/report/checkout3.png")

   