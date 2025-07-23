'''
telefone = '(86)98764-7645'

if telefone.find('89') == -1:   
    print('Outro DDD')
else:
    print('DDD 89')

nome = 'Yuri Moreira'
print(nome.strip())

nome2 = '           Yuri'
print(nome2.strip())

nome3 = 'Moreira                '
print(nome3.strip())
cep = '9877-065'
print(cep.replace('-', ' '))
print(cep.replace('-', ''))

nome = "Yuri"
sobrenome = "Moreira"

print(nome + " "  + sobrenome)
print(sobrenome + " " + nome)

text = 'Hello world!'
result = text[0:5]
print(result)

result2 = text[:3]
print(result2)
text = 'How are you doing today'
text_array = text.split(" ")
print(text)
print(text_array)
print(text[0])
print(text_array[0])
'''
nome_completo = 'Yuri Kauan Ibiapino Moreira'
print(nome_completo.upper())
print(nome_completo.lower())
