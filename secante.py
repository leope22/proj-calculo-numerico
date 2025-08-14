def secante(f, x0, x1, tol, max_iter):
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            print("Denominador zero. Não é possível continuar.")
            return None
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x_new - x1) < tol:
            print("Convergência alcançada.")
            return x_new
        x0, x1 = x1, x_new
    print("Número máximo de iterações atingido.")
    return x1

f = lambda x: x**3 - 9*x + 3
x0 = 0
x1 = 1
tol = 1e-6
max_iter = 100

raiz = secante(f, x0, x1, tol, max_iter)
print("A raiz encontrada é:", raiz)