#Daniel Caldana Jeveaux - 3TII
#Igor Jorge Ferraz - 3TII
#Juliano Breda de Oliveira - 3TII

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

#ler o arquivo carros.txt para adquirir as informações, que devem estar sepadas por vírgula dentro dele, exemplo 
#VOLKSWAGEN, VOLKSWAGEN VOYAGE 1.6 MSI FLEX 16V 4P AUT, 2019, Automático, Sedã, Prata, 49999, Vila Velha
def leArquivo(path):
    with open(path, 'r') as file:
        data = file.readlines()
        carros = [line.strip().split(", ") for line in data]
        return carros

#Cadastro e Login do usuário
def cadastro_usuario(driver, username, email, password):
    username_field = driver.find_element(By.ID, "username")
    username_field.clear()
    username_field.send_keys(username)
    username_field.send_keys(Keys.RETURN)

    email_field = driver.find_element(By.ID, "email")
    email_field.clear()
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)

    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys(password)

    password_confirm_field = driver.find_element(By.NAME, "passwordConfirm")
    password_confirm_field.clear()
    password_confirm_field.send_keys(password)

    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.send_keys(Keys.RETURN)

    time.sleep(5)

    login_link = driver.find_element(By.TAG_NAME, "a")
    login_link.click()

    username_login = driver.find_element(By.ID, "username")
    username_login.clear()
    username_login.send_keys(username)
    username_login.send_keys(Keys.RETURN)

    password_login = driver.find_element(By.ID, "password")
    password_login.clear()
    password_login.send_keys(password)
    password_login.send_keys(Keys.RETURN)

    time.sleep(3)

    login_button = driver.find_element(By.TAG_NAME, "button")
    login_button.send_keys(Keys.RETURN)

#Cadastro dos Carros que estão no documento carros.txt, os elementos devem estar separados por virgulas no documento
def realizaCadastro(driver, carro):
    marca = driver.find_element(By.ID, "marca")
    marca.clear()
    marca.send_keys(carro[0])

    modelo = driver.find_element(By.ID, "modelo")
    modelo.clear()
    modelo.send_keys(carro[1])

    ano = driver.find_element(By.ID, "ano")
    ano.clear()
    ano.send_keys(carro[2])

    cambio_automatico = driver.find_element(By.ID, "cambioAutomatico")
    if carro[3].lower() == "automático":
        cambio_automatico.click()

    sedan = driver.find_element(By.ID, "c_sedan")
    if carro[4].lower() == "sedã":
        sedan.click()

    hatch = driver.find_element(By.ID, "c_hatch")
    if carro[4].lower() == "hatch":
        hatch.click()

    cor = driver.find_element(By.ID, "cor")
    cor.send_keys(carro[5])

    valor = driver.find_element(By.ID, "valor")
    valor.clear()
    valor.send_keys(carro[6])

    municipio = driver.find_element(By.ID, "municipio")
    municipio.clear()
    municipio.send_keys(carro[7])

    button = driver.find_element(By.NAME, "insert")
    button.send_keys(Keys.RETURN)

    time.sleep(3)

    new = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button")
    new.send_keys(Keys.RETURN)

#Caminho absoluto do documento carros.txt, antes do o, so funcionava na máquina local
current_dir = os.path.dirname(os.path.abspath(__file__))
rel_path = "carros.txt"
abs_file_path = os.path.join(current_dir, rel_path)
carros = leArquivo(abs_file_path)

#ligação com o chromium
driver = webdriver.Chrome()
driver.get("http://weka.inf.ufes.br/IFESTP/index.php")

#Cadastro do usuário
cadastro_usuario(driver, "Rapadura", "igordanieljuliano@tii.com", "20212023idj")

#Repeticao para cadastrar carros até o final da lista
for carro in carros:
    realizaCadastro(driver, carro)

assert "No results found." not in driver.page_source
driver.close()
