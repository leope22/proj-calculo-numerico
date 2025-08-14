def fatoracao_cholesky(matriz):
    n = len(matriz)
    
    L = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1):
            soma = sum(L[i][k] * L[j][k] for k in range(j))
            
            if i == j:
                L[i][j] = (matriz[i][i] - soma) ** 0.5
            else:
                L[i][j] = (matriz[i][j] - soma) / L[j][j]
    
    return L

matriz = [
    [4, 8, 4],
    [8, 20, 20],
    [4, 20, 65]
]

L = fatoracao_cholesky(matriz)

print("Matriz L:")
for linha in L:
    print(linha)