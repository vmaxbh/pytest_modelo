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

def test_click_Produtos(log_in):
    cartBackpack = log_in.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']")
    cartBackpack.click()
    time.sleep(1)
    print('Produto 1 selecionado com Sucesso!')
    cartBackpack = log_in.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']")
    cartBackpack.click()
    time.sleep(1)
    print('Produto 2 selecionado com Sucesso!')
    cartBackpack = log_in.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']")
    cartBackpack.click()
    time.sleep(1)
    print('Produto 3 selecionado com Sucesso!')
    cartBackpack = log_in.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']")
    cartBackpack.click()
    time.sleep(1)
    print('Produto 4 selecionado com Sucesso!')
    cartBackpack = log_in.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']")
    cartBackpack.click()
    time.sleep(1)
    print('Produto 5 selecionado com Sucesso!')
    cartBackpack = log_in.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']")
    cartBackpack.click()
    time.sleep(1)
    log_in.get_screenshot_as_file("testsChrome/1-home-page/report/produtos1.png")
    print('Produto 6 selecionado com Sucesso!')
    cart_count_element = log_in.find_element(By.XPATH, "//*[@class='fa-layers-counter shopping_cart_badge']")
    cart_count_text = cart_count_element.text
    assert cart_count_text == "6", "O número de itens no carrinho não é igual a 6."
    print('Valor de itens selecionados confirmado junto ao componente com Sucesso, 6 Produtos Selecionados!')
    log_in.get_screenshot_as_file("testsChrome/1-home-page/report/produtos2.png")
    


    
   
     
    
    
 

