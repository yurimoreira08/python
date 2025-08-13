import random

numero_secreto = random.randint(0, 100)
numero_escolhido = int(input("Em apenas 10 tentativas adivinhe o número de 0 a 100: "))
tentativa = 1

while tentativa <= 10:
    if numero_escolhido == numero_secreto:
        print("Parabéns! Você acertou.")
        break
    elif numero_escolhido < numero_secreto:
        print("Tente um número maior.")
    else: 
        print("Tente um número menor")
    tentativa += 1
    if tentativa <= 10:
        numero_escolhido = int(input(f"Essa é sua {tentativa}º tentativa. Tente novamente: "))
        continue
    else:
        print("Suas tentativas acabaram.")
        
    


