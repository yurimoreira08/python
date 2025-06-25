#For e For
quant = int(input("Digite quantas vezes você quer calcular o fatorial: "))

for i in range(quant):
    fatorial = 1
    numero = int(input("Digite o número que você quer calcular: "))
    for i in range(1, numero + 1):
        fatorial *= i
    print(fatorial)
 
#While e For
contador = 0
quant = int(input("Digite quantas vezes você quer calcular o fatorial: "))

while quant > contador:
    fatorial = 1
    numero = int(input("Digite o número que você quer calcular: "))
    for i in range(1, numero + 1):
        fatorial *= i
    print(fatorial)
    contador += 1

#For e While
quant = int(input("Digite quantas vezes você quer calcular o fatorial: "))

for i in range(1, quant + 1):
    fatorial = 1
    numero = int(input("Digite o número que você quer calcular: "))
    while i <= numero:
        fatorial *= i
        i += 1
    print(fatorial)

#While e While
contador = 0
quant = int(input("Digite quantas vezes você quer calcular o fatorial: "))

while quant > contador:
    i = 1
    fatorial = 1
    numero = int(input("Digite o número que você quer calcular: "))
    while i <= numero:
        fatorial *= i
        i += 1
    print(fatorial)
    contador += 1 


