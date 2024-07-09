from datetime import datetime, timedelta
from armazenamento_busca import armazenar_dados, buscar_registros
from utilitarios import data_atual, data_horario_valido, exibir_opcoes_menu, exibir_titulo, filtrar_por_condicao, input_obrigatorio, pausa, retornar_ao_menu, validar_dados

formato_data = "%d/%m/%Y %H:%M"
campos = ["Título", "Descrição", "Local", "Data do evento", "Lembrete definido para"]

def agenda():
    exibir_titulo("Agenda")

    print("Olá! Aqui você pode agendar compromissos relacionados ao cuidado de seus animais.")

    lembretes()

    lista = ["1. Adicionar novo evento à agenda", "2. Verificar a agenda completa deste mês", "0. Retornar ao menu"]
    opcoes = {
         '0': retornar_ao_menu,
         '1': adicionar,
         '2': agenda_mes
    }

    exibir_opcoes_menu(opcoes, lista)
    
def adicionar():
    print("Adiconar um novo evento:\n")

    titulo = input_obrigatorio("Defina um título para o envento: ")
    descricao = input("Adicione uma breve descrição (opcional): ")
    local = input("Adicione um local (opcional): ")

    data = validar_dados("Informe a data do evento no formato 'DD/MM/AAAA HH:mm': ", data_horario_valido, "Por favor, informe uma data válida no formato especificado.")

    data_passada = diferenca_datas(data_atual(formato_data), data)
    
    if data_passada:
        print("\nNão é possível agendar eventos para datas e horários já passados. Retornando ao menu da agenda...")
        return pausa(2)
    
    data = datetime.strptime(data, formato_data)

    print("Gostaria de definir um lembrete personalizado? Selecione uma das opções abaixo:\n")
    print("1. Não quero definir lembrete (serei lembrado apenas no horário do evento)")
    print("2. Uma hora antes")
    print("3. Um dia antes")
    print("4. Três dias antes")

    opcao = input("\nSelecione uma opção: ")

    lembretes = {'1': timedelta(), '2': timedelta(hours=-1), '3': timedelta(days=-1), '4': timedelta(days=-3)}
    data_lembrete = data + lembretes.get(opcao, timedelta())

    if opcao not in lembretes:
        print("Opção inválida. Não será definido um lembrete.\n")

    data_lembrete = data_lembrete.strftime(formato_data)
    data = data.strftime(formato_data)

    dados = f"{titulo};{descricao};{local};{data};{data_lembrete}\n"
    armazenar_dados("agenda.csv", dados)

    print("\nEvento registrado com sucesso!\n")

def agenda_mes():
    print("\nAqui estão todos os eventos planejados para esse mês:\n")
    eventos_mes = filtrar_por_condicao(buscar_registros("agenda.csv"), meses_iguais, 3)
    eventos_ordenados = sorted(eventos_mes, key=lambda X: datetime.strptime(X[3], '%d/%m/%Y %H:%M'))

    imprimir_lista(eventos_ordenados) if eventos_ordenados else print("\nNão há nada programado ainda.\n")

def lembretes():
    print("\nLembretes:")
    print('-' * 20 + '\n')

    eventos= buscar_registros("agenda.csv")
    lembretes = filtrar_por_condicao(eventos, dia_e_horas_iguais, 4)

    imprimir_lista(lembretes) if lembretes else print("\nNão há nenhum lembrete programado para agora.")
    print('\n')

def imprimir_lista(lista, campos=campos):
    for evento in lista:
        for i, item in enumerate(evento):
            print(f"{campos[i]}: {item}")
        print('-' * 30)

def diferenca_datas(data_1, data_2):
    dif = (datetime.strptime(data_2, formato_data) - datetime.strptime(data_1, formato_data)).total_seconds()
    return dif <= 0

def meses_iguais(dado):
    try:
        return datetime.strptime(dado, "%d/%m/%Y %H:%M").month == datetime.now().month
    except:
        return datetime.strptime(dado, "%d/%m/%Y").month == datetime.now().month

def dia_e_horas_iguais(dado):
    #corta a string no comprimento desejado
    return dado[:13] == data_atual("%d/%m/%Y %H")