contatos = []
continuar = True

while continuar:
    print('''
          --- Agenda de Contatos ---
          1. Adicionar Contato
          2. Listar Contatos
          3. Buscar Contato por Nome
          4. Remover Contato por Nome
          5. Sair
          ''')

    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 1:
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")

            contato = {
                "nome": nome,
                "telefone": telefone,
                "email": email
            }

            contatos.append(contato)
            print("Contato adicionado com sucesso!\n")

        case 2:
            if contatos:
                print("\n--- Lista de Contatos ---")
                for c in contatos:
                    print(f"Nome: {c['nome']}, Telefone: {c['telefone']}, Email: {c['email']}")
            else:
                print("Nenhum contato cadastrado.\n")

        case 3:
            nome_busca = input("Digite o nome do contato que deseja buscar: ").lower()
            encontrado = False
            for c in contatos:
                if c["nome"].lower() == nome_busca:
                    print(f"\nContato encontrado: Nome: {c['nome']}, Telefone: {c['telefone']}, Email: {c['email']}")
                    encontrado = True
            if not encontrado:
                print("Contato não encontrado.\n")

        case 4:
            nome_remover = input("Digite o nome do contato que deseja remover: ").lower()
            removido = False
            for c in contatos:
                if c["nome"].lower() == nome_remover:
                    contatos.remove(c)
                    print("Contato removido com sucesso.\n")
                    removido = True
                    break
            if not removido:
                print("Contato não encontrado.\n")

        case 5:
            print("Saindo da agenda...")
            continuar = False

        case _:
            print("Opção inválida. Tente novamente.")
