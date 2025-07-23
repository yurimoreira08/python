# Dimensões do céu
linhas = 10
colunas = 40

while True:
    print("\n=== CÉU ESTRELADO ===")

    try:
        qtd = int(input("Quantas estrelas você quer desenhar? "))
        simbolo = input("Qual símbolo você quer usar como estrela? ")

        # Criar céu vazio
        ceu = []
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                linha.append(" ")
            ceu.append(linha)

        # Espalhar estrelas de forma irregular
        colocadas = 0
        for i in range(linhas):
            for j in range(colunas):
                if colocadas >= qtd:
                    break
                # fórmula irregular que espalha bem
                if (i * 3 + j * 17) % 2 == 0:
                    ceu[i][j] = simbolo
                    colocadas += 1

        # Imprimir céu
        print("\nSeu céu estrelado:\n")
        for linha in ceu:
            for celula in linha:
                print(celula, end="")
            print()

    except:
        print("Erro: Digite um número inteiro válido.")
