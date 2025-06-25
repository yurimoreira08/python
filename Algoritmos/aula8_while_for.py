'''
num = 0
print("Início!")
while num < 10:
    print(num)
    num += 1
print("Fim!")

num_inteiro = 1
cont, r = 0, 0
while cont < 5:
    r = num_inteiro * 3
    print(f"O triplo e: {r}")
cont += 1

for x in range(10):
	print("Linha ", x)

print("While:")
cont = 0
while cont < 5:
    x = 1
    r = x * 3
    print(r)
    cont += 1
    
print("\nFor:")

for cont in range(5):
    x = 1
    r = x * 3
    print(r)
'''
x = 2
y = 8
z = 1

cont = 0
while cont < y:
    z *= x
    cont += 1
print(f"O potência de {x} elevado a {y} é {z}")


x = 2
y = 5
z = 1

for i in range(y):
    z *= x
print(f"O potência de {x} elevado a {y} é {z}")
    