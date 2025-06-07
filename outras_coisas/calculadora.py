calculo = input("""1- Adição
2- Subitração
3- Multiplicação
4- Divisão 
Escolha uma opção: """)
num1 = int(input("Digite aqui o primeiro número: "))
num2 = int(input("Digite aqui o segundo número: "))

match calculo:
    case "1":
        print("O resultado é: ", num1 + num2)
    case "2":
        print("O resultado é: ", num1 - num2)
    case "3":
        print("O resultado é: ", num1 * num2)
    case "4":
        print("O resultado é: ", num1 / num2)