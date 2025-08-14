def eliminacao_gauss(matriz, termos_independentes):
    n = len(matriz)
    
    for i in range(n):
        linha_max = i
        for k in range(i + 1, n):
            if abs(matriz[k][i]) > abs(matriz[linha_max][i]):
                linha_max = k
        
        matriz[i], matriz[linha_max] = matriz[linha_max], matriz[i]
        termos_independentes[i], termos_independentes[linha_max] = termos_independentes[linha_max], termos_independentes[i]

        for k in range(i + 1, n):
            fator = matriz[k][i] / matriz[i][i]
            termos_independentes[k] -= fator * termos_independentes[i]
            for j in range(i, n):
                matriz[k][j] -= fator * matriz[i][j]
    
    solucao = [0] * n
    
    for i in range(n - 1, -1, -1):
        solucao[i] = termos_independentes[i]
        for j in range(i + 1, n):
            solucao[i] -= matriz[i][j] * solucao[j]
        solucao[i] /= matriz[i][i]
    
    return solucao

matriz = [
    [1, 2, -1],
    [2, -1, 3],
    [-3, 4, 2]
]

termos_independentes = [3, 7, -1]

solucao = eliminacao_gauss(matriz, termos_independentes)
print("Solução:", solucao)