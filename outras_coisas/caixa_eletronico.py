amarelo = "\033[33m"
reset = "\033[0m"
saldo = 2000

while True:
    print("\n*** Bem-vindo ao Banco Virtual ***")
    print(f"Seu saldo atual é de: R$ {saldo:.2f}")
    print("---------------------------------\n")
    print("Escolha uma opção:")
    print("1. Consultar Saldo")
    print("2. Sacar Dinheiro")
    print("3. Depositar Dinheiro")
    print("4. Sair")
    
    opcao = int(input(">"))

    match opcao:
        case 1:
            print(f"{amarelo}Seu saldo atual é de R$ {saldo:.2f}{reset}")
        case 2:
            saque = float(input(f"{amarelo}Digite o valor para saque: R$ "))
            if saque > saldo:
                print(f"{amarelo}Saldo insuficiente!{reset}")
            else:
                saldo -= saque
                print(f"{amarelo}Saque realizado com sucesso.{reset}")
                print(f"{amarelo}Novo saldo: R$ {saldo:.2f}{reset}")
        case 3:
            deposito = float(input(f"{amarelo}Digite o valor para depósito: R$ "))
            saldo += deposito
            print(f"{amarelo}Depósito realizado com sucesso.{reset}")
            print(f"{amarelo}Novo saldo: R$ {saldo:.2f}{reset}")
        case 4:
            print(f"{amarelo}Obrigado por usar nossos serviços. Volte sempre!{reset}")
            break
        case _:
            print(f"{amarelo}Opção inválida! Tente novamente.{reset}")
