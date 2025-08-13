import random

frutas = ["banana", "maçã", "melão", "mamão"]

continuar = True
while continuar:
    print('''
========== SORTEADOR DE FRUTAS ==========
1 - Jogar adivinhe a fruta
2 - Sair

''')
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        fruta_secreta = random.choice(frutas)
        
        tentativa = input("Digite uma fruta: ").lower()
        
        if tentativa == fruta_secreta:
            print("Parabéns, Você acertou!")
        else:
            print("Errou!")
            
            letras_em_comum = set(tentativa) & set(fruta_secreta)
            
            if letras_em_comum:
                print("Letras em comum:", "".join(sorted(letras_em_comum)))
                
            else:
                print("Nenhuma letra em comum.")
                
    elif opcao == 2:
        print("Jogo encerrado.")
        continuar = False
    else:
        print("Opção inválida! Tente novamente.")