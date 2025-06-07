'''
O Desafio: Crie um programa em Python para calcular o bônus que um vendedor receberá com base no valor de suas vendas mensais.
As Regras: O programa deve solicitar ao usuário o valor total das vendas do mês. O bônus será calculado de acordo com a seguinte tabela:
Vendas até R$ 10.000: Bônus de 5% sobre o valor das vendas.
Vendas de R$ 10.001 a R$ 50.000: Bônus de 7.5% sobre o valor das vendas.
Vendas acima de R$ 50.000: Bônus de 10% sobre o valor das vendas.
A Saída: Ao final, o programa deve exibir a mensagem: "Seu bônus este mês é de R$ X", onde X é o valor do bônus calculado.
'''

vendas = float(input("Qual o valor total das vendas do mês?"))

if vendas <= 10000:
    bonus = vendas * (5/100)
elif vendas >= 10001 and vendas <= 50000:
    bonus = vendas * (7.5/100)
else:
    bonus = vendas * (10/100)
    
print(f"Seu bônus este mês é de R$ {bonus:.2f}")
