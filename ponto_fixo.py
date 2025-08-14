def ponto_fixo(g, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            print("Convergência alcançada.")
            return x_new
        x = x_new
    print("Número máximo de iterações atingido.")
    return x

g = lambda x: ((20*x + 7) / 2)**(1/3)
x0 = 1.5
tol = 1e-6
max_iter = 100

raiz = ponto_fixo(g, x0, tol, max_iter)
print("A raiz encontrada é:", raiz)