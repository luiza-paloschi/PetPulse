from cadastrar_animal import cadastrar_animal
from listar_animais import listar_animais
from agenda import agenda
from diario_comportamental import diario_comportamental
from dieta_exercicio import dieta_exercicio
from diario_gastos import diario_gastos
from utilitarios import exibir_opcoes_menu

def titulo():
    arte = f"""  
  ____      _   ____        _          
 |  _ \ ___| |_|  _ \ _   _| |___  ___ 
 | |_) / _ \ __| |_) | | | | / __|/ _ \\
 |  __/  __/ |_|  __/| |_| | \__ \  __/
 |_|   \___|\__|_|    \__,_|_|___/\___|
                                                                  
    """
    print(arte)

def sair():
    print("Encerrando o programa...")

def menu():
    titulo()
    print("Olá, seja bem-vindo(a) ao PetPulse!\n\n")

    opcoes = {
        '1': cadastrar_animal,
        '2': listar_animais,
        '3': agenda,
        '4': diario_comportamental,
        '5': dieta_exercicio,
        '6': diario_gastos,
        '0': sair
    }

    lista = ["1. Cadastrar um animal", "2. Listagem de animais", "3. Agenda", "4. Diário de comportamento",
             "5. Dieta e exercício", "6. Diário de gastos", "0. Sair"]

    exibir_opcoes_menu(opcoes, lista)

menu()