def leArquivo(path):
    with open(path, 'r') as file:
        data = file.readlines()
        carros = [line.strip().split(", ") for line in data]
        return carros

abs_path = r"C:\Users\igorj\Documents\MEU\ESCOLA - IFES\3 ANO\AD\py\Py\carros.txt"
carros = leArquivo(abs_path)
print(carros)

