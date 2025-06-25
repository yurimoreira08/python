a, b, c = 3, 4, 5
def triangulo_valido(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        if a == b and b == c:
            print("O triângulo é equilátero!")
        elif a == b or b == c or c == a:
            print("O triângulo é isósceles!")
        else:
            print("O triângulo é escaleno!")
    else:
        print("O triângulo é impossível!")    
triangulo_valido(a, b, c)

x, y = 10, 10
def area_terreno(x, y):
    area = x * y
    print("A área do terreno é", area)
area_terreno(x, y)

r = 5
def area_circunferencia(r):
    area = 3.14 * (r**2)
    print("A área da circunferência é", area)
area_circunferencia(r)