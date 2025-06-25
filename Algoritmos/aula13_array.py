continuar = True
dados = []
while continuar:
    entrada = input("Digite sim para preencher dados ")
    if entrada == "sim":
        dados.append(input("Digite o nome: "))
        dados.append(input("Digite o sobrenome: "))
        dados.append(input("Digite o altura: "))
        dados.append(input("Digite o peso: "))
        print(dados)
        continuar = True
    else:
        print("Encerrado.")
        continuar = False