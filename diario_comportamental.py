from armazenamento_busca import armazenar_dados, buscar_registros_por_nome
from utilitarios import animal_existe, data_atual, exibir_opcoes_menu, exibir_titulo, input_obrigatorio, retornar_ao_menu
from collections import defaultdict

def diario_comportamental():
    exibir_titulo("Diário comportamnetal")

    opcoes = {'0': retornar_ao_menu, '1': adicionar_registro, '2': exibir_registros}
    lista = (["0. Retornar ao menu", "1. Adicionar um novo registro no diário", "2. Exibir o diário de um animal"])
    
    exibir_opcoes_menu(opcoes, lista)

def adicionar_registro():
    print("\nAdicionar um novo registro no diário:\n")
   
    animal = animal_existe("Informe o NOME de um animal para vincular ao registro: ")
    if not animal:
        return
    
    registro = input_obrigatorio("Digite suas observações em relação ao comportamento do animal:\n")
    data_registro = data_atual("%d/%m/%Y")

    dados = f"{animal[0]};{data_registro};{registro}\n"
    armazenar_dados("comportamento.csv", dados)
    print("\nRegistro adicionado com sucesso!")
    
def exibir_registros():
    print("\nMostrar as anotações registradas:\n")
   
    animal = animal_existe("Informe o NOME de um animal para ver seu diário: ")
    if not animal:
        return

    registros = buscar_registros_por_nome("comportamento.csv", animal[0])
    
    if not registros:
        return print("\nEste animal não possui nenhum registro de comportamento.\n")
    
    registros_dic = transformar_lista(registros)
 
    imprimir_dicionario(registros_dic)

def transformar_lista(lista_original):
     #ao tentar acessar uma chave que não existe, o defaultdict irá automaticamente gerar a chave e um valor padrão para ela, evitando um KeyError
    lista_formatada = defaultdict(list)

    for item in lista_original:
        _, data, registro = item
        lista_formatada[data].append(registro)
    
    return lista_formatada

def imprimir_dicionario(dic):
    print('\n'+ '-' * 30)
    for data, lista_registros in dic.items():
        print(f"{data}:\n")
        
        for index, registro in enumerate(lista_registros, 1):
            print(f"Registro {index} - {registro}")
        print('\n'+ '-' * 30)
    
    print("Fim dos registros.\n")