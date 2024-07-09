from armazenamento_busca import armazenar_dados, buscar_registros_por_nome, buscar_registros_hoje
from utilitarios import animal_existe, data_atual, exibir_opcoes_menu, exibir_titulo, retornar_ao_menu, valida_float, valida_int, validar_dados

def dieta_exercicio():
    exibir_titulo("Dieta e exercício")

    opcoes = {
         '0': retornar_ao_menu,
         '1': registrar,
         '2': historico
    }

    lista = (["1. Registrar peso ou atividade física", "2. Exibir o histórico de um animal", "0. Retornar ao menu"])
    
    exibir_opcoes_menu(opcoes, lista)

def registrar():
    animal = animal_existe("Informe o NOME de um animal para vincular ao registro: ")
    if not animal:
        return
    
    ja_registrou = buscar_registros_hoje("dieta_exercicio.csv", animal[0], data_atual("%d/%m/%Y"))
    if ja_registrou:
        return print("\nVocê só pode fazer um registro por dia para cada animal. Volte amanhã!\n")

    peso_atual = validar_dados("Informe o peso atual do animal (em kg): ", valida_float, "O peso deve ser um valor válido e maior que 0. Tente novamente.")
    atividade = validar_dados("Informe o número de minutos de atividade física praticada no dia de hoje: ", valida_int, "O número de minutos deve ser um inteiro maior ou igual a 0. Tente novamente.")

    data_registro = data_atual("%d/%m/%Y")

    dados = f"{animal[0]};{data_registro};{peso_atual};{atividade}\n"
    armazenar_dados("dieta_exercicio.csv", dados)
    print("\nRegistro adicionado com sucesso!")

def historico():
    animal = animal_existe("Informe o NOME de um animal para visualizar os registros: ")
    if not animal:
        return
    
    historico = buscar_registros_por_nome("dieta_exercicio.csv", animal[0])

    if not historico:
        return print("\nEsse animal não possui nenhum registro ainda.\n")
    
    peso_cadastro = animal[6]
    ultimo_registro = historico[len(historico) - 1]
    peso_final = ultimo_registro[2]

    soma = 0
    
    print(f"\nPeso informado no momento do cadastro: {peso_cadastro} kg")

    print('\n'+ '-' * 30)
    for registro in historico:
        _, data, peso, atividade = registro
        
        print(f"{data}:\n")
        print(f" - Peso (kg): {peso}")
        print(f" - Atividade física praticada (minutos): {atividade}")
        print('\n'+ '-' * 30)

        soma += int(registro[3])

    media = soma / len(historico)
    
    diferenca = float(peso_final) - float(peso_cadastro)

    if diferenca > 0:
        print(f"O seu animal ganhou {diferenca:.2f} kg desde o momento do cadastro.\n")
    elif diferenca < 0:
        print(f"O seu animal perdeu {-diferenca:.2f} kg  desde o momento do cadastro.\n")
    else:
        print("O peso do seu animal se manteve.\n")

    print(f"O animal pratica, em média, {media:.2f} minutos de exercício físico.\n")