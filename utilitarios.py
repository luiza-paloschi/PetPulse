import os
import time
from datetime import datetime
from armazenamento_busca import buscar_por_nome

def retornar_ao_menu():
    pausa(1.5)
    print("Retornando ao menu...")
    pausa(1)
    limpar_console()

def pausa(segundos):
    time.sleep(segundos)

def limpar_console():
    #cls para windows e clear para linux
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_titulo(titulo):
    linha = '*' * (len(titulo) + 4)
    print(f"\n{linha}\n* {titulo} *\n{linha}\n")

def input_obrigatorio(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada:
            return entrada
        else:
            print("Este campo é obrigatório. Por favor, insira um valor válido.")

def data_atual(formato):
    return datetime.now().strftime(formato);

def validar_dados(mensagem, funcao_validacao, mensagem_erro):
    while True:
        valor = input_obrigatorio(mensagem)
        if funcao_validacao(valor):
            return valor
        else:
            print(mensagem_erro + '\n')

def valida_int(valor):
        try:
            if int(valor) < 0:
                return False
            return True
        except ValueError:
            return False

def valida_float(valor):
        try:
            if float(valor) <= 0:
                return False
            return True
        except ValueError:
            return False

def data_horario_valido(data, formato='%d/%m/%Y %H:%M'):
    try:
        datetime.strptime(data, formato)
        return True
    except ValueError:
        return False
    
def filtrar_por_condicao(lista, condicao, campo):
    lista_filtrada = []
    for registro in lista:
        if condicao(registro[campo]):
            lista_filtrada.append(registro)
    return lista_filtrada

def exibir_opcoes_menu(opcoes, lista_opcoes):
    opcao = '1'
    while (opcao != '0'):
        
        print("Selecione uma das opções abaixo para prosseguir:\n")

        for texto in lista_opcoes:
            print(texto)

        opcao = input("\nDigite o número da opção escolhida: ")

        funcao = opcoes.get(opcao, opcao_invalida)
        funcao()

def opcao_invalida():
    print("\nOpção inválida. Por favor, tente novamente.\n")

def animal_existe(mensagem_input):
    nome = input_obrigatorio(mensagem_input)
    animal_cadastrado = buscar_por_nome("cadastro.csv", nome)
    if not animal_cadastrado:
        print("\nNão há nenhum animal cadastrado com esse nome.\n")

    return animal_cadastrado