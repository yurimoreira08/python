continuar = True 
while continuar:
    print('''
=============== MENU ===============
1: Descubra se o número é par ou ímpar
2: Imprima todos os números pares até um número
3: Imprima todos os números ímpares até um número
4: Imprima todos os números decrecentemente
5: Sair 
''')

    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        par_impar = int(input("Digite um número inteiro: "))
        if par_impar % 2 == 0:
            print("O número é par!")
        else:
            print("O número é ímpar!")
    elif opcao == 2:
        numeros_pares = int(input("Digite até qual número par você quer imprimir: "))
        for i in range(numeros_pares + 1):
            if i % 2 == 0:
                print(i)
    elif opcao == 3:
        numeros_impares = int(input("Digite até qual número ímpar você quer imprimir: "))
        for i in range(numeros_impares + 1):
            if i % 2 != 0:
                print(i)
    elif opcao == 4:
        decrescente = int(input("Digite o maior número a ser impresso: "))
        for i in range(decrescente, 0, -1):
            print(i)
    elif opcao == 5: 
        print("Programa encerrado!")
        continuar = False
    else:
        print("Digite uma opção válida")
        