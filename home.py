from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import re

def leArquivo(path):
    with open(path, 'r') as file:
        data = file.readlines()
        carros = [line.strip().split(", ") for line in data]
        return carros

abs_path = r"C:\Users\igorj\Documents\MEU\ESCOLA - IFES\3 ANO\AD\py\Py\carros.txt"
carros = leArquivo(abs_path)
print(carros)


driver = webdriver.Chrome()
driver.get("http://weka.inf.ufes.br/IFESTP/index.php")

#Cadastro e Login na plataforma, caso seja necessário.

username = driver.find_element(By.ID, "username")
username.clear()
username.send_keys("DanielSan2")
username.send_keys(Keys.RETURN) #se eu tirar sozinho não muda nada, mas se eu todos não loga

email = driver.find_element(By.ID, "email")
email.clear()
email.send_keys("noobhunter24@rusher.com")
email.send_keys(Keys.RETURN) 

password = driver.find_element(By.NAME, "password")
password.clear()
password.send_keys("red1709")

password_2 = driver.find_element(By.NAME, "passwordConfirm")
password_2.clear()
password_2.send_keys("red1709")

button = driver.find_element(By.NAME, "submit")
button.send_keys(Keys.RETURN) #se eu tirar não loga 

time.sleep(5)

login = driver.find_element(By.TAG_NAME, "a")
login.click()

username_login = driver.find_element(By.ID, "username")
username_login.clear()
username_login.send_keys("DanielSan2")
username_login.send_keys(Keys.RETURN) 

password_login = driver.find_element(By.ID, "password")
password_login.clear()
password_login.send_keys("red1709")
password_login.send_keys(Keys.RETURN) 

time.sleep(3)

button = driver.find_element(By.TAG_NAME, "button")
button.send_keys(Keys.RETURN) 
    
marca = driver.find_element(By.ID, "marca")
marca.clear()
marca.send_keys(carros[0][0])

modelo = driver.find_element(By.ID, "modelo")
modelo.clear()
modelo.send_keys(carros[0][1])

ano = driver.find_element(By.ID, "ano")
ano.clear()
ano.send_keys(carros[0][2])

cambio_automatico = driver.find_element(By.ID, "cambioAutomatico")
if carros[0][3].lower() == "automático":
    cambio_automatico.click()

sedan = driver.find_element(By.ID, "c_sedan")
if carros[0][4].lower() == "sedã":
    sedan.click()

hatch = driver.find_element(By.ID, "c_hatch")
if carros[0][4].lower() == "hatch":
    hatch.click()

cor = driver.find_element(By.ID, "cor")
cor.send_keys(carros[0][5])

valor = driver.find_element(By.ID, "valor")
valor.clear()
valor.send_keys(carros[0][6])

municipio = driver.find_element(By.ID, "municipio")
municipio.clear()
municipio.send_keys(carros[0][7])
    
button = driver.find_element(By.NAME, "insert")
button.send_keys(Keys.RETURN) 
    
time.sleep(3)   
    
assert "No results found." not in driver.page_source
driver.close()