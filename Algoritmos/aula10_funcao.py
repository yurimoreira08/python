def multiplica(x, y):
    z = x * y
    return z

def subtracao(x, y):
    z = x - y
    return z

def divisao(x, y):
    z = x / y
    return z

def potencia(x, y):
    z = x ** y
    return z

def fatorial(y):
    resultado = 1
    for i in range(1, y + 1):
        resultado *= i
    return resultado

print(multiplica(2, 5))
print(subtracao(8, 4))
print(divisao(10, 2))
print(potencia(2, 5))
print(fatorial(20))

