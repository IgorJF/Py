import os

def leArquivo(path):
    with open(path, 'r') as file:
        data = file.readlines()
        carros = [line.strip().split(", ") for line in data]
        return carros

# Obtendo o caminho do diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Combinando o caminho do diretório atual com o caminho relativo do arquivo
rel_path = "carros.txt"
abs_file_path = os.path.join(current_dir, rel_path)

carros = leArquivo(abs_file_path)
print(carros) 
