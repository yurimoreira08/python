continuar = True
while continuar:
  print('''
  1: Inverta a ordem das letras das palavras
  2: Faça anagramas com a palavra
  3: Sair
  ''')
  opcao = int(input("Digite a opção desejada: "))

  if opcao == 1:
    texto = input("Digite uma palavra: ")
    texto_invertido = texto[::-1]
    print(f"O texto invertido é: {texto_invertido}")
  elif opcao == 2:
    palavra = input("Digite uma palavra: ")
    if len(palavra) <= 1:
      print(palavra)
    elif len(palavra) == 2:
      print(palavra, palavra[::-1])
    else:
      combinacao = ['']
      for letra in palavra:
        nova_combinacao = []
        for sequencia in combinacao:
          for posicao in range(len(sequencia)+1):
            nova_sequencia = sequencia[:posicao] + letra + sequencia[posicao:]
            nova_combinacao.append(nova_sequencia)
      combinacao = nova_combinacao
      print(set(combinacao))
  elif opcao == 3:
    print("Programa encerrado.")
    continuar = False
  else:
    print("Opção inválida.")