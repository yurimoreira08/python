nota1 = float(input("Digite a primeira nota bimestral: "))
nota2 = float(input("Digite a segunda nota bimestral: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado por média")
elif media < 7:
    prova_final = float(input("Digite a nota da prova final: "))
    if prova_final > 6:
        print("Aprovado em prova final")
    else:
        print("Reprovado")