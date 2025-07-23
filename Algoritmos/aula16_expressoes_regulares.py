import re

telefone = "+55(11)95148-2377"
padrao = "(\+?[0-9]{2,3})?(\([0-9]{2}\))([0-9]{4,5})(-)([0-9]{4})"
if re.match(padrao, telefone):
    print("Número de telefone válido")
else:
    print("Número de telefone inválido")
    
    