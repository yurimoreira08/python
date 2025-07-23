alunos = []

def dados_alunos():
    nome = input("Digite o nome do aluno: ")
    
    print("Notas do 1º bimestre:")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    
    print("Notas do 2º bimestre:")
    n3 = float(input("Nota 1: "))
    n4 = float(input("Nota 2: "))

    aluno = [
        [nome],
        [n1, n2],
        [n3, n4]
    ]
    
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

continuar = True
while continuar:
    print("\nEscolha uma opção:")
    print("1 - Imprimir boletins")
    print("2 - Lançar notas de alunos")
    print("3 - Sair")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        print("\n===== BOLETINS =====")
        for i in range(len(alunos)):
            print(f"\nAluno: {alunos[i][0][0]}")
            
            media1 = (alunos[i][1][0] + alunos[i][1][1]) / 2
            media2 = (alunos[i][2][0] + alunos[i][2][1]) / 2
            
            print(f"  1º Bimestre: {alunos[i][1][0]}, {alunos[i][1][1]} | Média: {media1:.2f}")
            print(f"  2º Bimestre: {alunos[i][2][0]}, {alunos[i][2][1]} | Média: {media2:.2f}")
            
            media_anual = (media1 + media2) / 2
            print(f"  Média Anual: {media_anual:.2f}")
            
            if media_anual >= 7:
                situacao = "Aprovado"
            elif media_anual >= 4:
                prova_final = float(input("  Nota da Prova Final: "))
                media_final = (media_anual + prova_final) / 2
                print(f"  Média Final: {media_final:.2f}")
                if media_final >= 6:
                    situacao = "Aprovado na Final"
                else:
                    situacao = "Reprovado"
            else:
                situacao = "Reprovado"
            
            print(f"  Situação: {situacao}")

    elif opcao == 2:
        dados_alunos()
        
    elif opcao == 3:
        print("Sistema de Notas encerrado!")
        continuar = False
        
    else:
        print("Escolha uma opção válida.")