linhas = 10
colunas = 40
continuar = True
while continuar:
    print('''
========== CÉU ESTRELADO ==========
1: Imprima símbolos que pareçam estrelas no céu
2: Escolha os símbolos que pareçam estrelas no céu
3: Sair
          ''')
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        quantidade_estrelas = int(input("Digite a quantidade de estrelas que você quer desenhar: "))
        simbolo = "⭐"
        ceu = []
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                linha.append(" ")
            ceu.append(linha)
            colocadas = 0
            for i in range(linhas):
                for j in range(colunas):
                    if colocadas > quantidade_estrelas:
                        break
                    if (i * 3 + j * 2) % 17 == 0:
                        ceu[i][j] = simbolo
                        colocadas += 1 
            print("\nSeu céu estrelado:\n")
            for linha in ceu:
                for celula in linha:
                    print(celula, end="")
                print()
    elif opcao == 2:
        pass
    elif opcao == 3:
        print("Programa encerrado!")
        continuar = False
    else: 
        print("Escolha uma opção válida.")