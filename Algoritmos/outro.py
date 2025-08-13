import re

usuarios = []

# Expressões regulares
regex_nome = r'^[A-Za-z\s]+$'
regex_endereco = r'^[A-Za-z\s]+$'
regex_cep = r'^\d{5}-?\d{3}$'
regex_telefone = r'^\(\d{2}\) \d{5}-\d{4}$'
regex_email = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def validar_usuario(usuario):
    erros = []
    if not re.match(regex_nome, usuario['nome']):
        erros.append('Nome inválido')
    if not re.match(regex_nome, usuario['sobrenome']):
        erros.append('Sobrenome inválido')
    if not re.match(regex_endereco, usuario['endereco']):
        erros.append('Endereço inválido')
    if not re.match(regex_cep, usuario['cep']):
        erros.append('CEP inválido')
    if not re.match(regex_telefone, usuario['telefone']):
        erros.append('Telefone inválido')
    if not re.match(regex_email, usuario['email']):
        erros.append('Email inválido')
    return erros

def cadastrar_usuario():
    print("\n--- Cadastro de novo usuário ---")
    campos = ['nome', 'sobrenome', 'endereco', 'cep', 'telefone', 'email']
    usuario = {}
    for campo in campos:
        while True:
            valor = input(f"{campo.capitalize()}: ").strip()
            if valor != "":
                usuario[campo] = valor
                break
            else:
                print("Campo obrigatório! Preencha novamente.")
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        print("\n--- Lista de Usuários ---")
        i = 0
        while i < len(usuarios):
            user = usuarios[i]
            print(f"{i + 1}. {user['nome']} {user['sobrenome']}")
            i += 1

def verificar_usuario():
    listar_usuarios()
    try:
        i = int(input("Escolha o número do usuário: ")) - 1
        if 0 <= i < len(usuarios):
            print("\n--- Dados do Usuário ---")
            user = usuarios[i]
            for chave in user:
                print(f"{chave.capitalize()}: {user[chave]}")
        else:
            print("Usuário inválido.")
    except:
        print("Entrada inválida.")

def validar_usuario_especifico():
    listar_usuarios()
    try:
        i = int(input("Escolha o número do usuário: ")) - 1
        if 0 <= i < len(usuarios):
            erros = validar_usuario(usuarios[i])
            if len(erros) == 0:
                print("Todos os campos estão corretos!")
            else:
                print("Erros encontrados:")
                for erro in erros:
                    print(f"- {erro}")
        else:
            print("Usuário inválido.")
    except:
        print("Entrada inválida.")

def editar_usuario():
    listar_usuarios()
    try:
        i = int(input("Escolha o número do usuário para editar: ")) - 1
        if 0 <= i < len(usuarios):
            print("\n--- Editando Usuário ---")
            for campo in usuarios[i]:
                atual = usuarios[i][campo]
                novo_valor = input(f"{campo.capitalize()} (atual: {atual}): ").strip()
                if novo_valor != "":
                    usuarios[i][campo] = novo_valor
            print("Usuário editado com sucesso!")
        else:
            print("Usuário inválido.")
    except:
        print("Entrada inválida.")

def relatorio_erros():
    print("\n--- Relatório de Cadastros com Erros ---")
    encontrou = False
    i = 0
    while i < len(usuarios):
        user = usuarios[i]
        erros = validar_usuario(user)
        if len(erros) > 0:
            encontrou = True
            print(f"\nUsuário {i + 1}: {user['nome']} {user['sobrenome']}")
            for erro in erros:
                print(f" - {erro}")
        i += 1
    if not encontrou:
        print("Todos os cadastros estão corretos!")

# Menu
while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários")
    print("3 - Verificar dados de um usuário")
    print("4 - Validar dados de um usuário")
    print("5 - Editar usuário")
    print("6 - Emitir relatório de erros")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        verificar_usuario()
    elif opcao == "4":
        validar_usuario_especifico()
    elif opcao == "5":
        editar_usuario()
    elif opcao == "6":
        relatorio_erros()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
