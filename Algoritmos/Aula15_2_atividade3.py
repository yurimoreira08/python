continuar = True
while continuar:
    print("1. número de letras da frase (sem espaços)")
    print("2. número de palavras da frase")
    print("3. sair")
    
    opcao = input("escolha uma opção: ")
    
    if opcao == "1":
        frase = input("digite uma frase: ")
        letras_sem_espaco = frase.replace(" ", "")
        print("número de letras (sem espaços):", len(letras_sem_espaco))
        
    elif opcao == "2":
        frase = input("digite uma frase: ")
        palavras = frase.split()
        print("número de palavras:", len(palavras))
        
    elif opcao == "3":
        print("Programa encerrado.")
        continuar = False
        
    else:
        print("Escolha uma opção válida.")