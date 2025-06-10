def nome_estado(numero):
    if numero == 1:
        return "Piauí"
    elif numero == 2:
        return "Maranhão"
    elif numero == 3:
        return "Ceará"
    elif numero == 4:
        return "Pernambuco"
    elif numero == 5:
        return "Alagoas"
    elif numero == 6:
        return "Rio Grande do Norte"
    elif numero == 7:
        return "Paraíba"
    elif numero == 8:
        return "Sergipe"
    elif numero == 9:
        return "Bahia"
    elif numero == 10:
        return "Amazonas"
    elif numero == 11:
        return "Pará"
    elif numero == 12:
        return "Amapá"
    elif numero == 13:
        return "Acre"
    elif numero == 14:
        return "Roraima"
    elif numero == 15:
        return "Rondônia"
    elif numero == 16:
        return "Tocantins"
    elif numero == 17:
        return "Goiás"
    elif numero == 18:
        return "Mato Grosso"
    elif numero == 19:
        return "Mato Grosso do Sul"
    elif numero == 20:
        return "Distrito Federal"
    elif numero == 21:
        return "São Paulo"
    elif numero == 22:
        return "Rio de Janeiro"
    elif numero == 23:
        return "Espírito Santo"
    elif numero == 24:
        return "Minas Gerais"
    elif numero == 25:
        return "Paraná"
    elif numero == 26:
        return "Santa Catarina"
    elif numero == 27:
        return "Rio Grande do Sul"
    else:
        return "Estado não existente"

continuar = True
while continuar:
    print('''
      Lista de estados do Brasil
      NORDESTE:         |   Norte:          |   CENTRO-OESTE:           |   SUDESTE:            |   SUL:
      1. Piauí          |   10. Amazonas    |   17. Goiás               |   21. São Paulo       |   25. Paraná
      2. Maranhão       |   11. Pará        |   18. Mato Grosso         |   22. Rio de Janeiro  |   26. Santa Catarina
      3. Ceará          |   12. Amapá       |   19. Mato Grosso do Sul  |   23. Espírito Santo  |   27. Rio Grande do Sul
      4. Pernambuco     |   13. Acre        |   20. Distrito Federal    |   24. Minas Gerais    |
      5. Alagoas        |   14. Roraima     |                           |                       |
      6. Rio G. do N.   |   15. Rondônia    |                           |                       |
      7. Paraíba        |   16. Tocantins   |                           |                       |
      8. Sergipe        |                   |                           |                       |
      9. Bahia          |                   |                           |                       |
      ''')

    numero = int(input("Número do estado que você mora: "))
    estado = nome_estado(numero)
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
        