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
    
def test_naoPreenchimentocheckout(log_in):
    cartBackpack = log_in.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']")
    cartBackpack.click()
    time.sleep(1)
    print('Produto 1 selecionado com Sucesso!')
    car = log_in.find_element(By.XPATH, "//*[@fill='currentColor']")
    car.click()
    print('btn Carrinho Clicado com Sucesso!')
    time.sleep(1)
    check = log_in.find_element(By.XPATH, "//*[@class='btn_action checkout_button']")
    check.click()
    print('btn checkout clicado com Sucesso!') 
    btnContinue = log_in.find_element(By.XPATH, "//*[@class='btn_primary cart_button']")
    btnContinue.click()  
    print('btn Continue clicado com Sucesso!') 
    time.sleep(2)
    error_message_element = log_in.find_element(By.XPATH, "//*[@data-test='error']")
    error_message_text = error_message_element.text
    expected_error_message = "Error: First Name is required"
    if error_message_text == expected_error_message:
        print(f"A mensagem de erro '{expected_error_message}' está presente na tela.")
    else:
        print(f"A mensagem de erro '{expected_error_message}' não está presente na tela ou é diferente da esperada.")
    time.sleep(5)
    print('Teste de não Validação do checkout perante o não preenchimento feito com Sucesso!')
    log_in.get_screenshot_as_file("testsEdge/2-checkout/report/naoPreenchimentocheckout1.png")