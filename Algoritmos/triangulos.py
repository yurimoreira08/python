def verificar_triangulo(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        if a == b and b == c:
            print("O triângulo é equilátero!")
        elif a == b or a == c or b == c:
            print("O triângulo é isósceles!")
        else:
            print("O triângulo é escaleno!")
    else:
        print("O triângulo não existe!")

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

verificar_triangulo(a, b, c)