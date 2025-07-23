contas = []
continuar = True
while continuar:
    print('''
=============== MENU ===============
1: Adicione a conta do mês
2: Imprima todas as contas do mês e a soma total
3: Imprima somente as contas maiores que um valor
4: Imprima somente as contas menores que um valor
5: Sair
''')
    opcao = int(input("Digite uma opção: "))
    
    if opcao == 1:
        nome_conta = input("Digite o nome da conta: ")
        valor_conta = float(input("Digite o valor da conta: "))
        conta = [nome_conta, valor_conta]
        contas.append(conta)
        print(f"A conta {nome_conta} foi adicionada com sucesso!")
    elif opcao == 2:
        print("\nContas do mês: ")
        soma_total = 0
        for conta in contas:
            nome = conta[0]
            valor = conta[1]
            print(f"{nome}: R$ {valor:.2f}")
            soma_total += valor
        print(f"Valor total das contas: {soma_total:.2f}")   
    elif opcao == 3:
        limite = float(input("Mostrar contas com o valor maior que: R$ "))
        print(f"\n=== Contas maiores que {limite:.2f} ===")
        tem_conta = False
        for conta in contas:
            if conta[1] > limite:
                print(f"{conta[0]}: R$ {conta[1]:.2f}")
                tem_conta = True
        if not tem_conta:
            print("Nenhuma conta maior que esse valor.")
    elif opcao == 4:
        limite2 = float(input("Mostrar contas com o valor menor que: R$ "))
        print(f"\n=== Contas menores que {limite2:.2f} ===")
        tem_conta2 = False
        for conta in contas:
            if conta[1] < limite2:
                print(f"{conta[0]}: R$ {conta[1]:.2f}")
                tem_conta2 = True
        if not tem_conta2:
            print("Nenhuma conta menor que esse valor.")
    elif opcao == 5:
        print("Programa encerrado!")
        continuar = False
    else:
        print("Digite uma opção válida.")   
        