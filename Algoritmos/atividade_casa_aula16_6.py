while True:
    print('Digite apenas os números de seu telefone, sem espaços e parênteses')
    telefone = input('Digite o telefone aqui: ')
    ddd = telefone[:2]
    
    if ddd == '86' or ddd == '89':
        print("Esse número é do Piauí!")
    else: 
        print('Esse número não é do Piauí!')
    if input('Deseja verificar outro número? S/N: ').lower() == 'n':
        print('Encerrado!')
        break

    
    