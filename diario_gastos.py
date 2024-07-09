from agenda import meses_iguais
from armazenamento_busca import armazenar_dados, buscar_registros
from diario_comportamental import imprimir_dicionario
from utilitarios import data_atual, exibir_opcoes_menu, exibir_titulo, filtrar_por_condicao, input_obrigatorio, retornar_ao_menu, valida_float, validar_dados
from collections import defaultdict

def diario_gastos():
    exibir_titulo("Diário de gastos")
    print("Registre os gastos com alimentos, medicamentos, suplementos e outros cuidados.\n")

    opcoes = { '0': retornar_ao_menu, '1': registrar_gasto,'2': historico_gastos}
    lista = (["0. Retornar ao menu", "1. Inscrever novo gasto", "2. Exibir o histórico do mês"])
    
    exibir_opcoes_menu(opcoes, lista)

def registrar_gasto():
    print("Adicionar uma nova despesa:\n")

    tipo = input_obrigatorio("Informe o tipo da despesa (ex: comida, consultas, brinquedos, etc.): ")
    valor = validar_dados("Informe o valor, em reais: ", valida_float, "O valor deve ser um número maior ou igual a 0. Tente novamente.")
    data = data_atual("%d/%m/%Y")

    dados = f"{data};{tipo};{valor}\n"
    armazenar_dados("gastos.csv", dados)

    print("\nRegistro adicionado com sucesso!\n")

def historico_gastos():
    print("Abaixo estão listadas as despesas do mês:")
    gastos_mes = filtrar_por_condicao(buscar_registros("gastos.csv"), meses_iguais, 0)
    gastos_mes_dic, total_gastos = transformar_dados(gastos_mes)

    if gastos_mes:
        imprimir_dicionario(gastos_mes_dic)
        print(f"Gasto total do mês: R${total_gastos:.2f}\n")
    else:
        print("\nNenhuma despesa registrada para este mês.\n")

def transformar_dados(lista_original):
    dicionario = defaultdict(list)
    soma = 0
    for item in lista_original:
        data, tipo, valor = item
        soma += float(valor)
        dicionario[data].append(f"Descrição: {tipo} - Valor: R${valor}")
    
    return dicionario, soma