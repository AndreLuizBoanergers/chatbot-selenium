from selenium import webdriver
import time
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(5)
user = 'xxxxx@gmail.com'
password = 'senha123'
campo_login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
campo_senha = '//*[@id="loginForm"]/div/div[2]/div/label/input'
login = driver.find_element(By.XPATH, campo_login)
login.click()
login.send_keys(user)
time.sleep(1)
senha = driver.find_element(By.XPATH,campo_senha)
senha.click();
senha.send_keys(password)
time.sleep(1)
senha.send_keys(Keys.ENTER);
time.sleep(10)
