numero = int(input("Digite aqui o número para verificar se é par ou ímpar: "))

if numero % 2 == 0:
    print("O número {} é par".format(numero))
elif numero % 2 == 1:
    print("O número {} é ímpar".format(numero))