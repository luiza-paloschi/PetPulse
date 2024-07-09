from utilitarios import retornar_ao_menu, exibir_titulo
from armazenamento_busca import buscar_registros

def listar_animais():
    exibir_titulo("Listagem de animais")
    lista_animais = buscar_registros("cadastro.csv")
    if not lista_animais:
        print("Não há nenhum animal cadastrado ainda!")
        return retornar_ao_menu()
    
    #armazena apenas o primeiro elemento de cada sub-lista, no caso, o nome do animal
    nomes = [animal[0].lower() for animal in lista_animais]
        
    for index, animal in enumerate(nomes, 1):
        print(f"{index} - {animal.capitalize()}")

    print(f"Total de animais cadastrados: {len(lista_animais)}\n")
 
    escolha = 'a'
    while escolha != '0':
        escolha = input("Informe o NOME de um animal para obter mais informações ou digite 0 (zero) para retornar ao menu: ").strip().lower()
        if escolha in nomes:
            indice = nomes.index(escolha)
            exibir_informacoes(lista_animais[indice])
        elif escolha != '0':
            print("Não há nenhum animal cadastrado com esse nome. Por favor, tente novamente.\n")

    retornar_ao_menu()

def exibir_informacoes(animal):

    dados = ["Nome", "Espécie", "Raça", "Idade (anos)", "Gênero", "Cor", "Peso (kg)", "Número do Microchip",
             "Nome do dono", "Contato do dono", "Notas adicionais", "Data de Cadastro"]
    
    for i, dado_animal in enumerate(animal):
        print(f"{dados[i]}: {dado_animal or 'Não informado'}")

    print("\n")           