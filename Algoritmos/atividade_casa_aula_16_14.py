def substituir_texto():
    texto = input("Digite o texto: ")
    alvo = input("Digite o trecho que deseja substituir: ")
    novo = input("Digite o novo texto: ")
    texto = texto.replace(alvo, novo)
    print("Texto atualizado:", texto)

def dividir_em_palavras():
    texto = input("Digite o texto: ")
    palavras = texto.split()
    print("Palavras no texto:", palavras)

def deixar_maiusculo():
    texto = input("Digite o texto: ")
    print("Texto em maiúsculo:", texto.upper())

while True:
    print("\n========== MENU ==========")
    print("1 - Substituir parte do texto")
    print("2 - Mostrar palavras separadas")
    print("3 - Colocar texto em MAIÚSCULO")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        substituir_texto()

    elif opcao == "2":
        dividir_em_palavras()

    elif opcao == "3":
        deixar_maiusculo()

    elif opcao == "4":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
