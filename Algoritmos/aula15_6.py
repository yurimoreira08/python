while True:
    print("\n=== PRODUTIVIDADE DE MILHO ===")
    print("1: Mostrar projeção de produtividade")
    print("2: Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
            inicial = float(input("Digite a produtividade inicial (em kg): "))
            aumento = float(input("Digite o aumento anual da produtividade (em kg): "))
            anos = int(input("Digite quantos anos quer fazer a projeção: "))

            print("\nProjeção de produtividade de milho:")
            produtividade = inicial
            for ano in range(1, anos + 1):
                print(f"Ano {ano}: {produtividade:.2f} kg")
                produtividade += aumento
    elif opcao == "2":
        print("Programa encerrado!")
        break
    else:
        print("Digite apenas opções válidas.")
