continuar = True
while continuar:
    print("1. formatar nome para crachá")
    print("2. formatar nome para email")
    print("3. sair")

    opcao = input("escolha uma opção: ")

    if opcao == "1":
        nome = input("digite o nome completo: ")
        print("nome para crachá:", nome.upper())

    elif opcao == "2":
        nome = input("digite o nome completo: ").strip().lower()
        empresa = input("digite o nome da empresa: ").strip().lower()
        partes = nome.split()
        primeiro = partes[0]
        ultimo = partes[-1]
        email = f"{primeiro}.{ultimo}@{empresa}.com"
        print("email:", email)

    elif opcao == "3":
        print("Programa encerrado.")
        continuar = False

    else:
        print("Escolha uma opção válida.")
