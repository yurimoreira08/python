lista = []
continuar = True
while continuar:
    entrada = input("Digite sim para preencher os dados: ")
    if entrada == "sim":
        dados = []
        dados.append(input("Digite o nome: "))
        dados.append(input("Digite o sobrenome: "))
        dados.append(input("Digite o altura: "))
        dados.append(input("Digite o peso: "))
        lista =  [dados]
        print(lista)
        continuar = True
    else:
        print("Encerrado.")
        continuar = False