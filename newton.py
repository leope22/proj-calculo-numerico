def newton_raphson(f, df, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Derivada zero. Não é possível continuar.")
            return None
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            print("Convergência alcançada.")
            return x_new
        x = x_new
    print("Número máximo de iterações atingido.")
    return x

f = lambda x: x**3 - 9*x + 3
df = lambda x: 3*x**2 - 9
x0 = 1.5
tol = 1e-6
max_iter = 100

raiz = newton_raphson(f, df, x0, tol, max_iter)
print("A raiz encontrada é:", raiz)