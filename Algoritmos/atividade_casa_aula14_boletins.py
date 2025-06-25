alunos = []
continuar = True
while continuar:
    print('''
1. Imprimir boletins
2. Lançar notas de alunos
3. Sair
          ''')
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        if not alunos:
            print("Nenhum aluno cadastrado ainda!")
        else:
            print("=== BOLETINS ===")
            for aluno in alunos:
                nome = aluno[0]
                b1_media = (aluno[1] + aluno[2]) / 2
                b2_media = (aluno[3] + aluno[4]) / 2

                print(f"Aluno: {nome}")
                print(f"1º Bimestre: Notas = {aluno[1]}, {aluno[2]} | Média = {b1_media:.2f}")
                print(f"2º Bimestre: Notas = {aluno[3]}, {aluno[4]} | Média = {b2_media:.2f}")
        
    elif opcao == 2:
        nome = input("Nome do aluno: ")
        nota1_b1 = float(input("Nota 1 do 1º bimestre: "))
        nota2_b1 = float(input("Nota 2 do 1º bimestre: "))
        nota1_b2 = float(input("Nota 1 do 2º bimestre: "))
        nota2_b2 = float(input("Nota 2 do 2º bimestre: "))
        aluno = [nome, nota1_b1, nota2_b1, nota1_b2, nota2_b2]
        alunos.append(aluno)
        print(f"Notas de {aluno} cadastrada com sucesso!")
        
    elif opcao == "3":
        print("Programa encerrado!")
        continuar = False

    else:
        print("Opção inválida. Tente novamente.")
