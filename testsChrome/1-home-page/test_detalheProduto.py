import pytest
import time
from commands.autenticacao import *
from selenium.webdriver.common.by import By
from commands.login_helpers import loginChrome

@pytest.fixture
def log_in():
    driver = loginChrome(username, password)  
    yield driver
    driver.quit()

def test_detalhe_Produtos(log_in):
    backpack = log_in.find_element(By.XPATH, "//*[@class='inventory_item_img']")
    backpack.click()
    print('Detalhamento do produto acessado através do Click na Imagem!')
    time.sleep(1)
    component = log_in.find_elements(By.XPATH, "//*[@class='inventory_details_desc']")
    
    if len(component) > 0 and component[0].is_displayed():
        print("O componente descritivo está visível na Tela!.")
    else:
        print("O componente descritivo não está visível ou não foi encontrado.")
    component = log_in.find_elements(By.XPATH, "//*[@class='inventory_details_img']")
    
    if len(component) > 0 and component[0].is_displayed():
        print("A Imagen do Produto está visível na Tela!.")
    else:
        print("A Imagen do Produto não está visível ou não foi encontrado.")    
    log_in.get_screenshot_as_file("testsChrome/1-home-page/report/detalheProduto0.png")    
    addCart = log_in.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']")
    addCart.click()
    print('ADD TO CART clicado com Sucesso!')
    sidebar = log_in.find_element(By.XPATH, "//*[@style='position: absolute; left: 0px; top: 0px; width: 100%; height: 100%; margin: 0px; padding: 0px; border: none; opacity: 0; font-size: 8px; cursor: pointer;']")
    sidebar.click()
    print('Sidebar acessado com Sucesso!')
    time.sleep(2)
    allItens = log_in.find_element(By.XPATH, "//*[@id='inventory_sidebar_link']")
    allItens.click()
    car = log_in.find_element(By.XPATH, "//*[@fill='currentColor']")
    car.click()
    print('btn Carrinho Clicado com Sucesso!')
    log_in.get_screenshot_as_file("testsChrome/1-home-page/report/detalheProduto1.png")
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
    log_in.get_screenshot_as_file("testsChrome/1-home-page/report/detalheProduto2.png")
    finish = log_in.find_element(By.XPATH, "//*[@class='btn_action cart_button']")
    finish.click()
    log_in.get_screenshot_as_file("testsChrome/1-home-page/report/detalheProduto3.png")
        
    time.sleep(5)    
    