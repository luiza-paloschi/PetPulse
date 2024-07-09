from utilitarios import retornar_ao_menu, exibir_titulo, input_obrigatorio, data_atual, validar_dados, valida_float
from armazenamento_busca import armazenar_dados, buscar_por_nome

def cadastrar_animal():
    exibir_titulo("Cadastro de Animais")
    print("Para cadastrar um animal, por favor forneça as seguintes informações:\n")
    
    while True:
        nome = input_obrigatorio("Nome do animal: ")
        animal_cadastrado = buscar_por_nome("cadastro.csv", nome)
        if animal_cadastrado:
            print(f"Já existe um animal cadastrado com o nome '{nome}'. Por favor, escolha outro nome.")
        else:
            break

    especie = input_obrigatorio("Espécie: ")
    raca = input("Raça (opcional): ").strip()
    idade = input_obrigatorio("Idade (anos): ")
    genero = input_obrigatorio("Gênero (masculino/feminino): ")
    cor = input("Cor/pelagem/plumagem (opcional): ").strip()
    peso = validar_dados("Peso (kg): ", valida_float, "Informe um valor válido")
    microchip = input("Número do microchip (se houver): ").strip()
    dono = input_obrigatorio("Nome do dono: ")
    contato_dono = input_obrigatorio("Contato do dono (telefone/e-mail): ")
    notas_adicionais = input("Notas adicionais: ").strip()
    data_cadastro = data_atual("%d/%m/%Y")

    dados = f"{nome};{especie};{raca};{idade};{genero};{cor};{peso};{microchip};{dono};{contato_dono};{notas_adicionais};{data_cadastro}\n"
    armazenar_dados("cadastro.csv", dados)
    
    print("\nAnimal cadastrado com sucesso!")
    retornar_ao_menu()