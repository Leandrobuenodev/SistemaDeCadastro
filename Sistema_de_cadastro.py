cadastro = {
    "12345678900": {
        "nome": "João Silva",
        "idade": 30,
        "email": "joao.silva@email.com",
        "endereco": "Rua A, 123"
    },
    "98765432100": {
        "nome": "Maria Oliveira",
        "idade": 25,
        "email": "maria.oliveira@email.com",
        "endereco": "Avenida B, 456"
    },
    "11122233344": {
        "nome": "Carlos Souza",
        "idade": 40,
        "email": "carlos.souza@email.com",
        "endereco": "Praça C, 789"
    }
}

def cadastro_usuario():
    cpf = input("Digite o CPF do cliente: ").strip()
    if cpf in cadastro:
        print("CPF já está cadastrado.")
    else:
        print("Cliente não cadastrado. Iniciando cadastro.")
        nome = input("Digite o nome: ").strip()
        idade = input("Digite a idade: ").strip()
        email = input("Digite o email: ").strip()
        endereco = input("Digite o endereço: ").strip()

        cadastro[cpf] = {
            "nome": nome,
            "idade": idade,
            "email": email,
            "endereco": endereco
        }

        print("Dados salvos com sucesso!\n")

def menu():
    while True:
        print("\nO que você deseja fazer?")
        print("[1] Fazer novo cadastro")
        print("[2] Sair")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            cadastro_usuario()
        elif escolha == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()
