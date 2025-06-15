produtos = []


continuar = True
while continuar:
    print('''
          --- Agenda de Contatos ---
          1. Adicionar produtos
          2. Listar produtos
          3. Remover produto
          4. Atualizar quantidade
          5. Calcular valor total
          6. Sair
          ''')
    escolha = int(input("Digite aqui a sua escolha: "))
    
    match escolha:
        case 1:
            nome = str(input("Digite o nome do produto: ")).upper()
            quantidade = int(input("Digite o quantidade do produto: "))
            preco = float(input("Digite o preço do produto: "))
            
            produto = {
                "nome": nome,
                "quantidade": quantidade,
                "preco": preco
            }
            
            produtos.append(produto)
            
            print("Seu produto foi adicionado com sucesso!")
        case 2:
            if produtos:
                for p in produtos:
                    print(f"Nome: {p["nome"]}, Quantidade: {p["quantidade"]}, Preço: {p["preco"]}")
            else:
                print("Nenhum produto cadastrado")
        case 3:
            remover = input("Digite o nome do produto que deseja remover: ").upper()
            encontrado = False
            for p in produtos:
                if p["nome"] == remover:
                    produtos.remove(p)
                    print("O produto foi removido com sucesso.")
                    encontrado = True
                    break
            if not encontrado:
                print("Produto não encontrado.")
        case 4:
            buscar = input("Digite o nome do produto que deseja atualizar a quantidade: ").upper()
            encontrado = False
            for p in produtos:
                if p["nome"] == buscar:
                    nova_qtd = int(input(f"Quantidade atual: {p['quantidade']}. Digite a nova quantidade: "))
                    p["quantidade"] = nova_qtd
                    print("Quantidade atualizada com sucesso!")
                    encontrado = True
                    break  
            if not encontrado:
                print("Produto não encontrado.")
        case 5:
            if produtos:
                total = 0
                for p in produtos:
                    subtotal = p["quantidade"] * p["preco"]  
                    total += subtotal  
                print(f"\nValor total do estoque: R${total:.2f}\n") 
            else:
                print("Não há produtos cadastrados no estoque.")
        case 6:
            print("Programa finalizado")
            continuar = False
                    
    