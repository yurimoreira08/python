import re

usuarios = []

padrao_nome = r'^[A-Za-z\s]+$'
padrao_endereco = r'^[A-Za-z\s]+$'
padrao_cep = r'^\d{5}-?\d{3}$'
padrao_telefone = r'([0-9]{2,3})?(\([0-9]{2}\))([0-9]{4,5})([0-9]{4})'
padrao_email = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def validar_usuario(usuario):
    erros = []
    if not re.match(padrao_nome, usuario[0]):
        erros.append('Nome inválido')
    if not re.match(padrao_nome, usuario[1]):
        erros.append('Sobrenome inválido')
    if not re.match(padrao_endereco, usuario[2]):
        erros.append('Endereço inválido')
    if not re.match(padrao_cep, usuario[3]):
        erros.append('CEP inválido')
    if not re.match(padrao_telefone, usuario[4]):
        erros.append('Telefone inválido')
    if not re.match(padrao_email, usuario[5]):
        erros.append('Email inválido')
    return erros

def cadastrar_usuario():
    print("\n--- Cadastro de novo usuário ---")
    campos = ['Nome', 'Sobrenome', 'Endereço', 'CEP', 'Telefone', 'Email']
    usuario = []
    for campo in campos:
        while True:
            valor = input(f"{campo}: ").strip()
            if valor != "":
                usuario.append(valor)
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
            print(f"{i + 1}. {usuarios[i][0]} {usuarios[i][1]}")
            i += 1

def verificar_usuario():
    listar_usuarios()
    i = int(input("Escolha o número do usuário: ")) - 1
    if 0 <= i < len(usuarios):
        print("\n--- Dados do Usuário ---")
        print(f"Nome: {usuarios[i][0]}")
        print(f"Sobrenome: {usuarios[i][1]}")
        print(f"Endereço: {usuarios[i][2]}")
        print(f"CEP: {usuarios[i][3]}")
        print(f"Telefone: {usuarios[i][4]}")
        print(f"Email: {usuarios[i][5]}")
        erros = validar_usuario(usuarios[i])
        if len(erros) == 0:
            print("Todos os campos estão corretos.")
        else:
            print("Erros encontrados:")
            for erro in erros:
                print(f"- {erro}")
    else:
        print("Usuário inválido.")

def editar_usuario():
    listar_usuarios()
    i = int(input("Escolha o número do usuário para editar: ")) - 1
    if 0 <= i < len(usuarios):
        print("\n--- Editando Usuário ---")
        campos = ['Nome', 'Sobrenome', 'Endereço', 'CEP', 'Telefone', 'Email']
        for j in range(6):
            atual = usuarios[i][j]
            novo_valor = input(f"{campos[j]} (atual: {atual}): ").strip()
            if novo_valor != "":
                usuarios[i][j] = novo_valor
        print("Usuário editado com sucesso!")
    else:
        print("Usuário inválido.")

def relatorio_erros():
    print("\n--- Relatório de Cadastros com Erros ---")
    encontrou = False
    i = 0
    while i < len(usuarios):
        erros = validar_usuario(usuarios[i])
        if len(erros) > 0:
            encontrou = True
            print(f"\nUsuário {i + 1}: {usuarios[i][0]} {usuarios[i][1]}")
            for erro in erros:
                print(f" - {erro}")
        i += 1
    if not encontrou:
        print("Todos os cadastros estão corretos!")

while True:
    print("\n===== MENU =====")
    print("1: Cadastrar novo usuário")
    print("2: Listar usuários")
    print("3: Verificar dados de um usuário")
    print("4: Editar usuário")
    print("5: Relatório")
    print("6: Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        verificar_usuario()
    elif opcao == "4":
        editar_usuario()
    elif opcao == "5":
        relatorio_erros()
    elif opcao == "6":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
