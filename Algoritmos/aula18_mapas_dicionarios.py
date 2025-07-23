'''
meu_dict = dict(nome = "Arthur", idade = 999, pais = "Brasil")

meu_dict.update({"Altura": 1.7, "Sexo": "Virgem"})
meu_dict.update({"nome": "Yuri", "Sexo": "Só com Arthur", "ex": "Ianzoka"})
print(meu_dict.get("nome"))

ifpi = {
    "Mateus": "careca",
    "Lorrany": 29087738,
    "Yuri": "comedor de asiático",
    "Arthur": "asiático"
}
print(ifpi)
'''

carro = {}
carro["cor"] = "Prata"
carro["marca"] = "Fiat"
carro["modelo"] = "Uno"
carro["ano"] = "2012"

carro["cor"] = "Vermelha"
carro["ano"] = "2014"
carro.pop("ano")

for k in carro.keys():
    print(k)    