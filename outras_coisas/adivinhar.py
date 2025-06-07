import random

numero_secreto = random.randint(1, 10)
tentativa = int(input("Adivinhe o número de 1 a 10: "))

while tentativa != numero_secreto:
    if tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
    tentativa = int(input("Tente novamente: "))

print("Parabéns! Você acertou.")
