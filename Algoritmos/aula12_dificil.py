def nome_estado(abreviacao):
    if abreviacao == "pi" or abreviacao == "PI":
        capital = "Teresina"
        return "Piauí", capital
    elif abreviacao == "ma" or abreviacao == "MA":
        capital = "São Luís"
        return "Maranhão", capital
    elif abreviacao == "ce" or abreviacao == "CE":
        capital = "Fortaleza"
        return "Ceará", capital
    elif abreviacao == "pe" or abreviacao == "PE":
        capital = "Recife"
        return "Pernambuco", capital
    elif abreviacao == "al" or abreviacao == "AL":
        capital = "Maceió"
        return "Alagoas", capital
    elif abreviacao == "rn" or abreviacao == "RN":
        capital = "Natal"
        return "Rio Grande do Norte", capital
    elif abreviacao == "pb" or abreviacao == "PB":
        capital = "João Pessoa"
        return "Paraíba", capital
    elif abreviacao == "se" or abreviacao == "SE":
        capital = "Aracaju"
        return "Sergipe", capital
    elif abreviacao == "ba" or abreviacao == "BA":
        capital = "Salvador"
        return "Bahia", capital
    elif abreviacao == "am" or abreviacao == "AM":
        capital = "Manaus"
        return "Amazonas", capital
    elif abreviacao == "pa" or abreviacao == "PA":
        capital = "Belém"
        return "Pará", capital
    elif abreviacao == "ap" or abreviacao == "AP":
        capital = "Macapá"
        return "Amapá", capital
    elif abreviacao == "ac" or abreviacao == "AC":
        capital = "Rio Branco"
        return "Acre", capital
    elif abreviacao == "rr" or abreviacao == "RR":
        capital = "Boa Vista"
        return "Roraima", capital
    elif abreviacao == "ro" or abreviacao == "RO":
        capital = "Porto Velho"
        return "Rondônia", capital
    elif abreviacao == "to" or abreviacao == "TO":
        capital = "Palmas"
        return "Tocantins", capital
    elif abreviacao == "go" or abreviacao == "GO":
        capital = "Goiânia"
        return "Goiás", capital
    elif abreviacao == "mt" or abreviacao == "MT":
        capital = "Cuiabá"
        return "Mato Grosso", capital
    elif abreviacao == "ms" or abreviacao == "MS":
        capital = "Campo Grande"
        return "Mato Grosso do Sul", capital
    elif abreviacao == "df" or abreviacao == "DF":
        capital = "Brasília"
        return "Distrito Federal", capital
    elif abreviacao == "sp" or abreviacao == "SP":
        capital = "São Paulo"
        return "São Paulo", capital
    elif abreviacao == "rj" or abreviacao == "RJ":
        capital = "Rio de Janeiro"
        return "Rio de Janeiro", capital
    elif abreviacao == "es" or abreviacao == "ES":
        capital = "Vitória"
        return "Espírito Santo", capital
    elif abreviacao == "mg" or abreviacao == "MG":
        capital = "Belo Horizonte"
        return "Minas Gerais", capital
    elif abreviacao == "pr" or abreviacao == "PR":
        capital = "Curitiba"
        return "Paraná", capital
    elif abreviacao == "sc" or abreviacao == "SC":
        capital = "Florianópolis"
        return "Santa Catarina", capital
    elif abreviacao == "rs" or abreviacao == "RS":
        capital = "Porto Alegre"
        return "Rio Grande do Sul", capital
    else:
        capital = "Desconhecida"
        return "Estado não existente", capital


continuar = True
while continuar:
  print('''
      Lista de estados do Brasil
      NORDESTE:           |   NORTE:           |   CENTRO-OESTE:        |   SUDESTE:             |   SUL:
      PI - Piauí          |   AM - Amazonas    |   GO - Goiás           |   SP - São Paulo       |   PR - Paraná
      MA - Maranhão       |   PA - Pará        |   MT - Mato Grosso     |   RJ - Rio de Janeiro  |   SC - Santa Catarina
      CE - Ceará          |   AP - Amapá       |   MS - Mato G. do Sul  |   ES - Espírito Santo  |   RS - Rio G. do Sul
      PE - Pernambuco     |   AC - Acre        |   DF - Dist. Federal   |   MG - Minas Gerais    |
      AL - Alagoas        |   RR - Roraima     |                        |                        |
      RN - Rio G. do N.   |   RO - Rondônia    |                        |                        |
      PB - Paraíba        |   TO - Tocantins   |                        |                        |
      SE - Sergipe        |                    |                        |                        |  
      BA - Bahia          |                    |                        |                        |
      ''')

  abreviacao = input("Abreviação do estado que você mora: ")
  estado, capital = nome_estado(abreviacao)
  if estado == "Estado não existente":
      print(estado)
  else:
      print(f"Você mora no estado {estado}, sua capital é {capital}")
        
  entrada = input("Digite sim para continuar: ")
  if entrada == "sim":
      print("Quer continuar!")
      continuar = True
  else:
      print("Não quer continuar!")
      continuar = False