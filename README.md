# Projetos de Cálculo Numérico

Implementações em Python de métodos numéricos para solução de:

* **Zeros de Funções Reais:** Encontrar raízes de equações ($f(x)=0$).
* **Sistemas Lineares:** Resolver sistemas de equações ($Ax=b$).
* **Equações Diferenciais Ordinárias:** Solução de problemas de valor inicial (PVI).

## 1. Zeros de Funções Reais

### Métodos
* **Bissecção:** Garante a convergência dividindo o intervalo ao meio.
* **Ponto Fixo:** Baseado na iteração de uma função $x=g(x)$.
* **Newton-Raphson:** Usa a derivada (reta tangente) para convergência rápida.
* **Secante:** Aproxima a derivada com uma reta secante, rápido e prático.

### Análise Comparativa
Resultados para encontrar a raiz de $f(x) = x^3 - 9x + 3$ no intervalo (0, 1) com $\epsilon = 10^{-6}$:

* **Bissecção:** 19 iterações (Mais lento)
* **Ponto Fixo:** 7 iterações
* **Newton-Raphson:** 12 iterações (convergiu para outra raiz, 2.8169, devido ao chute inicial)
* **Secante:** 5 iterações (Mais rápido)

**Conclusão Geral:** Para funções polinomiais e não-polinomiais, os métodos de **Newton-Raphson** e da **Secante** foram consistentemente mais eficientes, exigindo menos iterações.

## 2. Sistemas Lineares

### Métodos
* **Eliminação de Gauss (Direto):** Transforma o sistema em uma matriz triangular.
* **Fatoração de Cholesky (Direto):** Decomposição $A=LL^T$ para matrizes simétricas.
* **Gauss-Jacobi (Iterativo):** Aproxima a solução a cada passo.
* **Gauss-Seidel (Iterativo):** Otimização de Gauss-Jacobi.

### Análise Comparativa
* **Métodos Diretos (Eliminação de Gauss):** Produziu a solução correta e precisa para os sistemas 3x3 e 10x10 testados.
* **Métodos Iterativos (Gauss-Jacobi/Seidel):** Falharam em convergir nos sistemas testados, pois o critério da diagonal dominante não foi satisfeito, resultando em valores impraticáveis.

## Extra: Equações Diferenciais Ordinárias (EDO)

Implementação do **Método de Euler** para resolver PVIs. O exemplo no código aplica o método à Lei de Resfriamento de Newton.
