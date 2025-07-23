def numero_primo(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

continuar = True
while continuar:
    print('''
========== MENU ==========
1: Imprima todos os números primos
2: Imprima todos os números primos menores que um número
3: Imprima todos os números primos maiores que um número   
4: Sair   
''')
    opcao = int(input("Digite aqui a opção desejada: "))
    
    if opcao == 1:
        quantidade_primos = int(input("Digite a quantidade de números primos a serem impressos: "))
        cont = 0
        numero = 2
        while cont < quantidade_primos:
            if numero_primo(numero):
                print(numero)
                cont += 1
            numero += 1

    elif opcao == 2:
        limite = int(input("Digite um número para imprimir os primos menores que esse número: "))
        for i in range(2, limite):
            if numero_primo(i):
                print(i)
    
    elif opcao == 3:
        limite2 = int(input("Digite um número para imprimir os 10 números primos maiores que esse número: "))
        numero2 = limite2 + 1
        cont2 = 0
        while cont2 < 10:
            if numero_primo(numero2):
                print(numero2)
                cont2 += 1
            numero2 += 1
            
    elif opcao == 4:
        print("Programa ecerrado!")
        continuar = False
    else:
        print("Digite apenas opções válidas.")