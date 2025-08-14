def gauss_jacobi(matriz, termos_independentes, precisao, max_iteracoes):
    n = len(matriz)
    x = [0.0 for _ in range(n)]
    
    for iteracao in range(max_iteracoes):
        novo_x = x.copy()
        
        for i in range(n):
            soma = sum(matriz[i][j] * x[j] for j in range(n) if j != i)
            
            novo_x[i] = (termos_independentes[i] - soma) / matriz[i][i]
        
        if max(abs(novo_x[i] - x[i]) for i in range(n)) < precisao:
            return novo_x
        
        x = novo_x
    
    return x

matriz = [
    [1, 2, -1],
    [2, -1, 3],
    [-3, 4, 2]
]

termos_independentes = [3, 7, -1]
precisao = 1e-10
max_iteracoes = 100
solucao = gauss_jacobi(matriz, termos_independentes, precisao, max_iteracoes)
print("Solução:", solucao)