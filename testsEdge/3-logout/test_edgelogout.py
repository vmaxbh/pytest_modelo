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
    nav = log_in.find_element(By.XPATH, "//*[@style='position: absolute; left: 0px; top: 0px; width: 100%; height: 100%; margin: 0px; padding: 0px; border: none; opacity: 0; font-size: 8px; cursor: pointer;']")
    nav.click()
    print('Pagina acessada com Sucesso!')
    time.sleep(1)
    log_in.get_screenshot_as_file("testsEdge/3-logout/report/logout1.png") 
    print('Sidebar acessado com Sucesso!')
    logout = log_in.find_element(By.XPATH, "//*[@id='logout_sidebar_link']")
    logout.click()
    print('Btn logout clicado com Sucesso!')
    log_in.get_screenshot_as_file("testsEdge/3-logout/report/logout2.png") 
    print('Logout Feito com Sucesso!')
    
    
    