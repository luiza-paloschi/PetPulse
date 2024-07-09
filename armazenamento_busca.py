import csv

def armazenar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'a', encoding='utf-8') as arq:
        arq.write(dados)

def buscar_por_nome(nome_arquivo, nome_animal):
    cadastro = []

    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arq:
            #cria um objeto reader que acessa o arquivo e retorna as linhas no formato de listas de strings
            leitor = csv.reader(arq, delimiter=';')
            for linha in leitor:
                if linha and linha[0].strip().lower() == nome_animal.strip().lower():
                    return linha
    except FileNotFoundError:
        pass
    
    return cadastro

def buscar_registros(nome_arquivo):
    registros = []
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            for linha in leitor:
                registros.append(linha)
    except FileNotFoundError:
        pass
    
    return registros

def buscar_registros_hoje(nome_arquivo, nome_animal, data_atual):
    registro = []

    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            for linha in leitor:
                if linha[0] == nome_animal and linha[1] == data_atual:
                    return linha
    except FileNotFoundError:
        pass
    
    return registro

def buscar_registros_por_nome(nome_arquivo, nome_animal):
    registros = []

    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            for linha in leitor:
                if linha[0] == nome_animal:
                    registros.append(linha)
    except FileNotFoundError:
        pass
    
    return registros