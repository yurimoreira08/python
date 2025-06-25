def fazer_pergunta(pergunta):
    resposta = input(pergunta + " (s/n): ").lower()
    if resposta == "s":
        return 1
    else:
        return 0

def interrogatorio():
    print("""
=== INTERROGATÓRIO POLICIAL ===
Responda com 's' para sim ou 'n' para não.
""")

    pontos = 0

    pontos += fazer_pergunta("Telefonou para a vítima?")
    pontos += fazer_pergunta("Esteve no local do crime?")
    pontos += fazer_pergunta("Mora perto da vítima?")
    pontos += fazer_pergunta("Devia dinheiro para a vítima?")
    pontos += fazer_pergunta("Já trabalhou com a vítima?")

    print("\nRESULTADO DA INVESTIGAÇÃO:")

    if pontos == 5:
        print("ASSASSINO!")
    elif pontos == 3 or pontos == 4:
        print("CÚMPLICE!")
    elif pontos == 2:
        print("SUSPEITO!")
    else:
        print("INOCENTE!")

def menu():
    while True:
        print("""
=== MENU ===
1. Iniciar interrogatório
2. Sair
""")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            interrogatorio()
        elif escolha == "2":
            print("Encerrando o sistema de investigação...")
            break
        else:
            print("Opção inválida.")

menu()
