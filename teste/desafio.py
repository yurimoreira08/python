def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def arranjo(n, p):
    return fatorial(n) // fatorial(n - p)

def combinacao(n, p):
    return fatorial(n) // (fatorial(p) * fatorial(n - p))

n = 5
p = 3

print(f"O arranjo de {n} e {p} é {arranjo(n, p)}")
print(f"A combinação de {n} e {p} é {combinacao(n, p)}")