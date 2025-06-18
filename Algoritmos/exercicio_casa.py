lista = []

print("\n===== CARDÁPIO =====")
print("1 - Pizza           (R$ 30.00)")
print("2 - Hambúrguer      (R$ 18.00)")
print("3 - Cachorro Quente (R$ 12.00)")
print("4 - Coxinha         (R$ 6.00)")
print("====================\n")

continuar = True

while continuar:
    entrada = input("Se você quer fazer um pedido digite 'sim': ").lower()

    if entrada == "sim":
        dados = []

        nome = input("Nome do cliente: ")
        lanche_codigo = int(input("Digite o número do lanche desejado: "))

        if lanche_codigo == 1:
            lanche = "Pizza"
            preco = 30.00
        elif lanche_codigo == 2:
            lanche = "Hambúrguer"
            preco = 18.00
        elif lanche_codigo == 3:
            lanche = "Cachorro Quente"
            preco = 12.00
        elif lanche_codigo == 4:
            lanche = "Coxinha"
            preco = 6.00
        else:
            print("Opção inválida.")
            continue

        qtd = int(input("Quantidade: "))
        taxa = float(input("Taxa de entrega (R$): "))

        subtotal = preco * qtd
        total = subtotal + taxa

        if total > 50:
            desconto = total * 0.1
            total -= desconto
        else:
            desconto = 0.0

        dados.append(nome)
        dados.append(lanche)
        dados.append(qtd)
        dados.append(preco)
        dados.append(taxa)
        dados.append(desconto)
        dados.append(total)

        lista = [dados]

        print("\nRESUMO DO PEDIDO")
        print(f"Cliente: {nome}")
        print(f"Lanche: {lanche}")
        print(f"Quantidade: {qtd}")
        print(f"Preço unitário: R$ {preco:.2f}")
        print(f"Taxa de entrega: R$ {taxa:.2f}")
        print(f"Desconto aplicado: R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

    else:
        print("Programa encerrado.")
        continuar = False
