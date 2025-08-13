# Tabuleiro vazio com 9 espaços
tabuleiro = [" "]*9

# Mostrar o tabuleiro
def mostrar():
    print(f"{tabuleiro[0]}|{tabuleiro[1]}|{tabuleiro[2]}")
    print("-+-+-")
    print(f"{tabuleiro[3]}|{tabuleiro[4]}|{tabuleiro[5]}")
    print("-+-+-")
    print(f"{tabuleiro[6]}|{tabuleiro[7]}|{tabuleiro[8]}")

# Verificar vitória
def venceu(jogador):
    c = tabuleiro
    return (
        (c[0] == c[1] == c[2] == jogador) or
        (c[3] == c[4] == c[5] == jogador) or
        (c[6] == c[7] == c[8] == jogador) or
        (c[0] == c[3] == c[6] == jogador) or
        (c[1] == c[4] == c[7] == jogador) or
        (c[2] == c[5] == c[8] == jogador) or
        (c[0] == c[4] == c[8] == jogador) or
        (c[2] == c[4] == c[6] == jogador)
    )

# Começa com o X
jogador = "X"

# Loop do jogo
for _ in range(9):
    mostrar()
    pos = int(input(f"Jogador {jogador}, escolha (0-8): "))
    if tabuleiro[pos] != " ":
        print("Ocupado! Tente outra.")
        continue
    tabuleiro[pos] = jogador
    if venceu(jogador):
        mostrar()
        print(f"{jogador} venceu!")
        break
    jogador = "O" if jogador == "X" else "X"
else:
    mostrar()
    print("Empate!")
