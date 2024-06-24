import pytest
import time
from commands.autenticacao import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.jira("KAN-9")   
def test_login():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080") 
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/index.html")
    print('Pagina acessada com Sucesso!')
    driver.get_screenshot_as_file("testsChrome/0-login/report/login1.png")
    username_field = driver.find_element(By.XPATH, "//*[@id='user-name']")  # Use By.ID aqui
    password_field = driver.find_element(By.XPATH, "//*[@id='password']")
    username_field.send_keys(username)
    print('Usuário incluido no campo com Sucesso!')
    password_field.send_keys(password)
    print('Password incluido no campo com Sucesso!')
    driver.get_screenshot_as_file("testsChrome/0-login/report/login2.png")
    btnLogin = driver.find_element(By.XPATH, "//*[@id='login-button']")
    btnLogin.click()
    time.sleep(5)
    app_logo = driver.find_element(By.XPATH, "//*[@class='app_logo']")
    assert app_logo.is_displayed(), "Componente.app_logo não está visível na página."  
    driver.get_screenshot_as_file("testsChrome/0-login/report/login3.png")
    print('Componente na tela inicial confirmado com Sucesso!')