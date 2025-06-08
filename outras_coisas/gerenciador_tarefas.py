import json
import os

def carregar_tarefas():
    if os.path.exists("tarefas.json"):
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else:
        return []

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

def listar_tarefas(tarefas):
    print("\n--- Sua Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa adicionada.")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "[X]" if tarefa["concluida"] else "[ ]"
        print(f"{status} {i}. {tarefa['descricao']}")

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    nova_tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f'Tarefa "{descricao}" adicionada!')

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        numero = int(input("Digite o número da tarefa a ser concluída: "))
        if 1 <= numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            salvar_tarefas(tarefas)
            print(f'Tarefa "{tarefas[numero - 1]["descricao"]}" marcada como concluída!')
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        numero = int(input("Digite o número da tarefa a ser removida: "))
        if 1 <= numero <= len(tarefas):
            tarefa_removida = tarefas.pop(numero - 1)
            salvar_tarefas(tarefas)
            print(f'Tarefa "{tarefa_removida["descricao"]}" removida com sucesso!')
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\nO que você gostaria de fazer?")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar como Concluída")
        print("4. Remover Tarefa")
        print("5. Salvar e Sair")

        opcao = input("> ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            salvar_tarefas(tarefas)
            print("Salvando alterações e saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
