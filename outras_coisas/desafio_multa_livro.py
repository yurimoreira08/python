print("Calculadora de multas.")
x = int(input("Quantos dias após o vencimento você devolveu o livro? "))
while x != 0:
    if x <= 3:
        R = x * 0.5
        print(f"Sua multa foi: R$ {R:.2f}")
        break
    elif x >= 4 and x <= 7:
        R = x * 1
        print(f"Sua multa foi: R$ {R:.2f}")
        break
    else:
        R = x * 2
        print(f"Sua multa foi: R$ {R:.2f}")
        break
  
