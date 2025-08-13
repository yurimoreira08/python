'''
Faça um sistema que:
Tenha um menu infinito usando WHILE com as opções:
Registre os dados de uma turma criando um código de turma em um mapa;
Registre os dados de um novo aluno com base na matrícula em um mapa;
Solicite preenher novamente se o campo estiver vazio;
Editar e sobrescrever os dados de um usuário cadastrado;
Emita um relatório com todas as turmas e seus alunos;
Mantenha mapas de mapas para armazenar os dados;
Use entrada de dados para capturar dados de turma:
Nivel de Ensino;
Módulo da turma;
Use entrada de dados para capturar dados dos usuários:
Nome do aluno;
Idade;
Use Math.randon para gerar código de turma e de matrícula;
'''
import random

turmas = {}
continuar = True
def criar_codigo():
  return random.randint(1000, 9999)

def solicitar_mensagem(msg):
    while continuar:
        valor = input(msg).strip
        if valor: 
            return valor
        else:
            print("Campo obrigatório. Tente novamente.")
            
def cadastrar_turma():
    nivel = solicitar_mensagem("Informe o nível de ensino da turma: ")
    modulo = solicitar_mensagem("Informe o módulo da turma: ")
    cod_turma = criar_codigo()
    
    turmas[cod_turma] = {
        "nivel": nivel,
        "modulo": modulo,
        "alunos": {}
    }
  
    print(f"Turma registrada com sucesso! Código da turma: {cod_turma}")

def cadastrar_alunos():
    cod_turma = solicitar_mensagem("Digite o código da turma: ")
    
    if cod_turma not in turmas:
        print("Turma não encontrada.\n")
        return
    nome = solicitar_mensagem("Digite o nome do aluno: ")
    idade = solicitar_mensagem("Digite a idade do aluno: ")
    matricula = criar_codigo()
    
    turmas[cod_turma]["alunos"][matricula] = {
        "nome": nome,
        "idade": idade,
    }
    
    print(f"Aluno cadastrado com matrícula: {matricula}")

def editar_aluno():
    cod_turma = solicitar_mensagem("Digite o código da turma: ")
    if cod_turma not in turmas:
        print("Turma não encontrada.\n")
        return
    
    matricula = solicitar_mensagem("Digite a matrícula do aluno: ")
    alunos = turmas[cod_turma]["alunos"]
    
    if matricula not in alunos:
        print("Aluno não encontrado.\n")
        return
    
    nome = solicitar_mensagem("Nome do aluno: ")
    idade = solicitar_mensagem("Idade do aluno: ")
    
    alunos[matricula] = {
        "nome": nome,
        "idade": idade
    }
    
    print("Dados editados com sucesso!\n")
        
def exibir_relatorio():
    if not turmas:
        print("Sem turma registrada!")
        return
    
    for cod_turma, turma in turmas.items():
        print(f"Turma {cod_turma} - {turma['nivel']} Módulo: ({turma['modulo']})")
        alunos = turma["alunos"]
        
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for matricula, aluno in alunos.items():
                print(f"-Matrícula {matricula}: {aluno['nome']}, {aluno['idade']} anos.")
        print()
        

def main():

  while True:
    print("\nMenu")
    print("1 - cadastrar nova turma")
    print("2 - cadastrar aluno")
    print("3 - editar dados")
    print("4 - exibir_Relatório")
    print("5 - sair ")

    opcao = input("escolha uma das opções. ").strip()

    if opcao == "1":
        cadastrar_turma()
    elif opcao == '2':
        cadastrar_alunos()
    elif opcao == "3":
        editar_aluno()
    elif opcao == "4":
        exibir_relatorio()
    elif opcao == "5":
        print("Programa encerrado.")
        break
    else:
        print("Digite uma opção válida")
main()

