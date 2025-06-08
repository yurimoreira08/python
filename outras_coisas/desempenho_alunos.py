amarelo = "\033[33m"
reset = "\033[0m"

lista_turma = []
quantidade_alunos = int(input("Quantos alunos você deseja cadastrar? "))

for x in range(quantidade_alunos):
    nome = input(f"Digite o nome do aluno {x + 1}: ")
    
    notas = []
    
    for y in range(1, 4):
        nota = float(input(f"Nota {y}: "))
        notas.append(nota)
    
    media = sum(notas) / 3

    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media
    }
    
    lista_turma.append(aluno)

soma_das_medias = 0
melhor_aluno = lista_turma[0]
pior_aluno = lista_turma[0]
aprovados = []
recuperacao = []
reprovados = []

for aluno in lista_turma:
    media = aluno["media"]
    soma_das_medias += media
    
    if media > melhor_aluno["media"]:
        melhor_aluno = aluno
    if media < pior_aluno["media"]:
        pior_aluno = aluno
        
    if media >= 7:
        aprovados.append(aluno["nome"])
    elif media >= 5.0:
        recuperacao.append(aluno['nome'])
    else:
        reprovados.append(aluno['nome'])
        
media_geral = soma_das_medias / quantidade_alunos

print("\n--- Relatório da Turma ---")
print(f"{amarelo}Média Geral da Turma: {media_geral:.2f}\n{reset}")

print(f"{amarelo}Aluno com Melhor Desempenho:{reset}")
print(f"{amarelo}- Nome: {melhor_aluno['nome']}{reset}")
print(f"{amarelo}- Média: {melhor_aluno['media']:.2f}\n{reset}")

print("Aluno com Pior Desempenho:")
print(f"{amarelo}- Nome: {pior_aluno['nome']}{reset}")
print(f"{amarelo}- Média: {pior_aluno['media']:.2f}\n{reset}")

print("--- Situação dos Alunos ---")
print(f"{amarelo}Aprovados: {aprovados}{reset}")
print(f"{amarelo}Recuperação: {recuperacao}{reset}")
print(f"{amarelo}Reprovados: {reprovados}{reset}")