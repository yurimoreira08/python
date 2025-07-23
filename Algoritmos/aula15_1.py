def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero"
    return x / y

continuar = True
while continuar:
    print("\n===== CALCULADORA =====")
    print("1 - Calcular o resultado")
    print("2 - Imprimir tabuada")
    print("3 - Sair")
    
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        n1 = int(input("Digite o primeiro número: "))
        operacao = input('''
Escolha a operação desejada:
+
-
*
/
Digite aqui: ''')
        n2 = int(input("Digite o segundo número: "))

        if operacao == "+":
            resultado = soma(n1, n2)
        elif operacao == "-":
            resultado = subtracao(n1, n2)
        elif operacao == "*":
            resultado = multiplicacao(n1, n2)
        elif operacao == "/":
            resultado = divisao(n1, n2)
        else:
            resultado = "Operação inválida"
        
        print(f"Resultado: {resultado}")

    elif opcao == 2:
        numero = int(input("Digite o número da tabuada que você quer imprimir: "))
        operacao = input('''
Escolha a operação desejada:
+
-
*
/
Digite aqui: ''')

        for i in range(1, 11):
            if operacao == "+":
                print(f"{numero} + {i} = {soma(numero, i)}")
            elif operacao == "-":
                print(f"{numero} - {i} = {subtracao(numero, i)}")
            elif operacao == "*":
                print(f"{numero} * {i} = {multiplicacao(numero, i)}")
            elif operacao == "/":
                print(f"{numero} / {i} = {divisao(numero, i):.2f}")
            else:
                print("Operação inválida.")
                break

    elif opcao == 3:
        print("Encerrando o programa...")
        continuar = False
    else:
        print("Opção inválida.")
