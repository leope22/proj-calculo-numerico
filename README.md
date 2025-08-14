# Projetos de Cálculo Numérico

Este repositório contém as implementações e análises de métodos numéricos:

1.  **Projeto 1: Zeros de Funções Reais** - Métodos para encontrar raízes de equações.
2.  **Projeto 2: Solução de Sistemas Lineares** - Métodos diretos e iterativos para resolver sistemas de equações lineares.
3.  **Extra: Solução de Equações Diferenciais Ordinárias (EDO)** - Implementação do Método de Euler.

## Projeto 1: Zeros de Funções Reais

Implementação e comparação de métodos para encontrar o zero de funções da forma $f(x) = 0$.

### Métodos Implementados

  * **Método da Bissecção:** Um método de busca incremental que divide o intervalo ao meio a cada iteração.
  * **Método do Ponto Fixo:** Transforma a equação $f(x)=0$ em uma forma equivalente $x=g(x)$ e itera a partir de uma aproximação inicial.
  * **Método de Newton-Raphson:** Utiliza a reta tangente ao gráfico da função para aproximar a raiz.
  * **Método da Secante:** Similar ao método de Newton, mas aproxima a derivada usando uma reta secante.

### Análise e Comparações

Os métodos foram aplicados e comparados em três funções distintas:

1.  **Função Polinomial 1:** $f(x) = x^3 - 9x + 3$

      * **Raiz no intervalo (0, 1) com precisão $\\epsilon = 10^{-6}$**
      * **Método da Secante:** Mais eficiente, convergiu em **5 iterações**.
      * **Método do Ponto Fixo:** Convergiu em **7 iterações**.
      * **Método de Newton-Raphson:** Convergiu em **12 iterações** para outra raiz (2.8169) devido à escolha do ponto inicial.
      * **Método da Bissecção:** Menos eficiente, necessitou de **19 iterações**.

2.  **Função Polinomial 2:** $f(x) = 2x^3 - 20x - 7$

      * Para a raiz no intervalo (3, 4), os métodos de Newton-Raphson (4 iterações) e da Secante (6 iterações) foram significativamente mais rápidos que os da Bissecção (19 iterações) e do Ponto Fixo (13 iterações).

3.  **Função Não Polinomial:** $f(x) = \\cos(x) - x$

      * Observou-se que métodos como Bissecção e Ponto Fixo exigiram um número consideravelmente maior de iterações em comparação com Newton-Raphson e Secante, reforçando a eficiência destes últimos.

## Projeto 2: Solução de Sistemas Lineares

Implementação e análise de métodos diretos e iterativos para resolver sistemas lineares da forma $Ax = b$.

### Métodos Implementados

  * **Método de Eliminação de Gauss:** Um método direto que transforma o sistema em uma forma triangular superior e resolve por substituição regressiva.
  * **Fatoração de Cholesky:** Um método direto para matrizes simétricas e positivas definidas, que decompõe a matriz $A$ em $A = LL^T$.
  * **Método Iterativo de Gauss-Jacobi:** Um método iterativo que aproxima a solução a cada passo.
  * **Método Iterativo de Gauss-Seidel:** Uma otimização do método de Gauss-Jacobi que utiliza os valores recém-calculados na mesma iteração.

### Análise e Comparações

  * **Sistema 3x3:** O método de Eliminação de Gauss foi o único que produziu a solução analítica correta. Os métodos iterativos (Gauss-Jacobi e Gauss-Seidel) não convergiram para a solução, resultando em valores extremamente grandes.
  * **Sistema 10x10:** Novamente, a Eliminação de Gauss forneceu uma solução precisa. Os métodos iterativos falharam em convergir, gerando resultados impraticáveis.

**Conclusão:** Para os sistemas testados, que não satisfaziam o critério de convergência (como o critério da diagonal dominante), os métodos iterativos não foram eficazes. O método direto de Eliminação de Gauss mostrou-se robusto e preciso.

## Extra: Solução de Equações Diferenciais Ordinárias (EDO)

Implementação do **Método de Euler** para resolver problemas de valor inicial em EDOs. O exemplo fornecido aplica o método à Lei de Resfriamento de Newton.
