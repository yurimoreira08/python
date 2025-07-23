n_b_alunos = [
    ["Fábio", [9,5], [5,7]],
    ["Aline", [7,8], [6,9]],
    ["Maria", [3,9], [4,6]]
]

'''
print(n_b_alunos)
print(n_b_alunos[1][2][0])
print(n_b_alunos[0][1][1])
print(n_b_alunos[2][1][0])

print((n_b_alunos[1][2][0] + n_b_alunos[1][2][1]) / 2)
print((n_b_alunos[0][1][0] + n_b_alunos[0][1][1]) / 2)
print((n_b_alunos[2][1][0] + n_b_alunos[2][1][1]) / 2)


b_1_Fabio = []
b_1_Fabio.append(9)
b_1_Fabio.append(5)
b_2_Fabio =[]
b_2_Fabio.append(5)
b_2_Fabio.append(7)
n_aluno = "Fabio"

aluno = []
aluno.append(n_aluno)
aluno.append(b_1_Fabio)
aluno.append(b_2_Fabio)
n_b_alunos= []
n_b_alunos.append(aluno)

print(n_b_alunos)
'''
'''
#Primeira nota de Aline no primeiro bimestre
print(n_b_alunos[1][1][0])

#Segunda nota de Fábio no segundo bimestre
print(n_b_alunos[0][2][1])

#Primeira nota de Maria no segundo bimestre
print(n_b_alunos[2][2][0])

#Imprimindo todos nomes dos alunos
for i in range (len(n_b_alunos)):
	for j in range (len(n_b_alunos[i])):
		print(n_b_alunos[i][j])
'''

for i in range(len(n_b_alunos)):
    print("i: ", i, "-", n_b_alunos[i][0], (n_b_alunos[i][1][0] + n_b_alunos[i][1][1]) / 2)