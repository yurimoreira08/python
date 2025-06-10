'''
def soma( x, y):
	return x + y

continuar = True
while(continuar):
  valor1 = int(input("Digite valor 1 para somar: "))
  valor2 = int(input("Digite valor 2 para somar: "))
  print("Resultado da soma:", soma(valor1, valor2))
  entrada = input("Digite sim para continuar: ")
  if (entrada == "sim"):
    print("Quer continuar.")
    continuar = True
  else :
    print("Não quer continuar.")
    continuar = False
'''

def lados_iguais(a, b, c):
    if a == b and b == c:
        return 3
    elif a == b or a == c or b == c:
        return 2
    else:
        return 0
continuar = True 
while continuar:
    a = input("Digite o lado a: ")
    b = input("Digite o lado b: ")
    c = input("Digite o lado c: ")
    quant_lados_iguais = lados_iguais(a, b, c)
    
    if quant_lados_iguais == 3:
        print("3 lados iguais!")
    elif quant_lados_iguais == 2:
        print("2 lados iguais!")
    else:
        print("Nenhum lado igual!")
    
    entrada = input("Digite sim para continuar: ")
    if entrada == "sim":
        print("Quer continuar!")
        continuar = True
    else:
        print("Não quer continuar!")
        continuar = False
        