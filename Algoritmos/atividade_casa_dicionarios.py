import random

turmas = {}

def gerar_codigo(prefixo=""):
    prefixo = input("Digite o prefixo da turma: ")
    return f"{prefixo}{random.randint(1000, 9999)}"

def solicitar_campo(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Campo obrigatório. Tente novamente.")

def registrar_turma():
    nivel = solicitar_campo("Informe o nível de ensino da turma: ")
    modulo = solicitar_campo("Informe o módulo da turma: ")
    cod_turma = gerar_codigo()

    turmas[cod_turma] = {
        "nivel": nivel,
        "modulo": modulo,
        "alunos": {}
    }

    print(f"Turma registrada com sucesso! Código da turma: {cod_turma}\n")

def registrar_aluno():
    cod_turma = solicitar_campo("Digite o código da turma: ")

    if cod_turma not in turmas:
        print("Turma não encontrada.\n")
        return

    nome = solicitar_campo("Digite o nome do aluno: ")
    idade = solicitar_campo("Digite a idade do aluno: ")
    matricula = gerar_codigo()

    turmas[cod_turma]["alunos"][matricula] = {
        "nome": nome,
        "idade": idade
    }

    print(f"Aluno cadastrado com matrícula: {matricula}\n")

def editar_aluno():
    cod_turma = solicitar_campo("Digite o código da turma: ")

    if cod_turma not in turmas:
        print("Turma não encontrada.\n")
        return

    matricula = solicitar_campo("Digite a matrícula do aluno: ")
    alunos = turmas[cod_turma]["alunos"]

    if matricula not in alunos:
        print("Aluno não encontrado.\n")
        return

    novo_nome = solicitar_campo("Novo nome do aluno: ")
    nova_idade = solicitar_campo("Nova idade do aluno: ")

    alunos[matricula] = {
        "nome": novo_nome,
        "idade": nova_idade
    }

    print("Dados do aluno atualizados com sucesso!\n")

def emitir_relatorio():
    print("\nRELATÓRIO DE TURMAS E ALUNOS:\n")

    if not turmas:
        print("Nenhuma turma cadastrada.\n")
        return

    for cod_turma, turma in turmas.items():
        print(f"Turma {cod_turma} - {turma['nivel']} Módulo:({turma['modulo']})")
        alunos = turma["alunos"]

        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for matricula, aluno in alunos.items():
                print(f"-Matrícula {matricula}: {aluno['nome']}, {aluno['idade']} anos")
        print()

while True:
    print('''
1 - Registrar dados da turma
2 - Registrar dados do aluno
3 - Editar dados
4 - Emitir relatório
5 - Sair
''')
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
            registrar_turma()
    elif opcao == 2:
            registrar_aluno()
    elif opcao == 3:
            editar_aluno()
    elif opcao == 4:
            emitir_relatorio()
    elif opcao == 5:
            print("Encerrando o programa.")
            break
    else:
        print("Opção inválida. Tente novamente.\n")