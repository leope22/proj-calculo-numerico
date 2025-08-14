def bisseccao(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("O teorema de Bolzano não é aplicável.")
        return None
    
    c = a
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

f = lambda x: 2*x**3 - 20*x - 7
a = 3
b = 4
tol = 1e-6

raiz = bisseccao(f, a, b, tol)
print("A raiz encontrada é:", raiz)