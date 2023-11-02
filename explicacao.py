# Importações das bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# Função para ler o arquivo 'carros.txt' e retornar os dados como uma lista
def leArquivo(path):
    with open(path, 'r') as file:
        data = file.readlines()
        carros = [line.strip().split(", ") for line in data]
        return carros

# Função para realizar o cadastro e login do usuário
def cadastro_usuario(driver, username, email, password):
    # Encontrar o campo de usuário e preencher com o nome de usuário fornecido
    # Encontrar o campo de e-mail e preencher com o e-mail fornecido
    # Encontrar o campo de senha e preencher com a senha fornecida
    # Encontrar o botão de enviar (submit) e clicar
    # Aguardar por 5 segundos
    # Clicar no link de login
    # Preencher o campo de usuário com o nome de usuário fornecido
    # Preencher o campo de senha com a senha fornecida
    # Clicar no botão de login
    # Aguardar por 3 segundos

# Função para realizar o cadastro de carros com base nos dados fornecidos
def realizaCadastro(driver, carro):
    # Encontrar e preencher o campo de marca com a marca do carro
    # Encontrar e preencher o campo de modelo com o modelo do carro
    # Encontrar e preencher o campo de ano com o ano do carro
    # Verificar se o carro possui câmbio automático e marcar o checkbox correspondente, se necessário
    # Verificar se o carro é um sedan e marcar o checkbox correspondente, se necessário
    # Verificar se o carro é um hatch e marcar o checkbox correspondente, se necessário
    # Encontrar e preencher o campo de cor com a cor do carro
    # Encontrar e preencher o campo de valor com o valor do carro
    # Encontrar e preencher o campo de município com o município do carro
    # Encontrar e clicar no botão de inserir (insert)
    # Aguardar por 3 segundos
    # Encontrar e clicar no botão 'novo' para limpar os campos e permitir um novo cadastro

# Obter o caminho absoluto do arquivo 'carros.txt'
current_dir = os.path.dirname(os.path.abspath(__file__))
rel_path = "carros.txt"
abs_file_path = os.path.join(current_dir, rel_path)
# Chamar a função leArquivo para ler o arquivo 'carros.txt' e armazenar os dados na variável carros
carros = leArquivo(abs_file_path)

# Iniciar o driver do navegador Chrome
driver = webdriver.Chrome()
# Abrir o site alvo
driver.get("http://weka.inf.ufes.br/IFESTP/index.php")

# Chamar a função cadastro_usuario para realizar o cadastro e login do usuário no site
cadastro_usuario(driver, "Rapadura", "igordanieljuliano@tii.com", "20212023idj")

# Loop para realizar o cadastro de cada carro na lista de carros
for carro in carros:
    realizaCadastro(driver, carro)

# Verificar se a string "No results found." não está presente na página
assert "No results found." not in driver.page_source

# Fechar a janela do navegador
driver.close()
