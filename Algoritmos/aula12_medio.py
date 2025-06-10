def nome_estado(abreviacao):
    if abreviacao == "pi" or abreviacao == "PI":
      return "Piauí"
    elif abreviacao == "ma" or abreviacao == "MA":
        return "Maranhão"
    elif abreviacao == "ce" or abreviacao == "CE":
        return "Ceará"
    elif abreviacao == "pe" or abreviacao == "PE":
        return "Pernambuco"
    elif abreviacao == "al" or abreviacao == "AL":
        return "Alagoas"
    elif abreviacao == "rn" or abreviacao == "RN":
        return "Rio Grande do Norte"
    elif abreviacao == "pb" or abreviacao == "PB":
        return "Paraíba"
    elif abreviacao == "se" or abreviacao == "SE":
        return "Sergipe"
    elif abreviacao == "ba" or abreviacao == "BA":
        return "Bahia"
    elif abreviacao == "am" or abreviacao == "AM":
        return "Amazonas"
    elif abreviacao == "pa" or abreviacao == "PA":
        return "Pará"
    elif abreviacao == "ap" or abreviacao == "AP":
        return "Amapá"
    elif abreviacao == "ac" or abreviacao == "AC":
        return "Acre"
    elif abreviacao == "rr" or abreviacao == "RR":
        return "Roraima"
    elif abreviacao == "ro" or abreviacao == "RO":
        return "Rondônia"
    elif abreviacao == "to" or abreviacao == "TO":
        return "Tocantins"
    elif abreviacao == "go" or abreviacao == "GO":
        return "Goiás"
    elif abreviacao == "mt" or abreviacao == "MT":
        return "Mato Grosso"
    elif abreviacao == "ms" or abreviacao == "MS":
        return "Mato Grosso do Sul"
    elif abreviacao == "df" or abreviacao == "DF":
        return "Distrito Federal"
    elif abreviacao == "sp" or abreviacao == "SP":
        return "São Paulo"
    elif abreviacao == "rj" or abreviacao == "RJ":
        return "Rio de Janeiro"
    elif abreviacao == "es" or abreviacao == "ES":
        return "Espírito Santo"
    elif abreviacao == "mg" or abreviacao == "MG":
        return "Minas Gerais"
    elif abreviacao == "pr" or abreviacao == "PR":
        return "Paraná"
    elif abreviacao == "sc" or abreviacao == "SC":
        return "Santa Catarina"
    elif abreviacao == "rs" or abreviacao == "RS":
        return "Rio Grande do Sul"
    else:
        return "Estado não existente"

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
  estado = nome_estado(abreviacao)
  if estado == "Estado não existente":
      print(estado)
  else:
      print(f"Você mora em {estado}")
        
  entrada = input("Digite sim para continuar: ")
  if entrada == "sim":
      print("Quer continuar!")
      continuar = True
  else:
      print("Não quer continuar!")
      continuar = False