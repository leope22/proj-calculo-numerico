import numpy as np

def f(temperatura, temp_ambiente, constante_k):
    return -constante_k * (temperatura - temp_ambiente)

def metodo_euler(temp_inicial, temp_ambiente, constante_k, tempo_final, num_subintervalos):

    passo_h = tempo_final / num_subintervalos
    valores_tempo = np.linspace(0, tempo_final, num_subintervalos + 1)
    valores_temperatura = np.zeros(num_subintervalos + 1)
    valores_temperatura[0] = temp_inicial
    
    print(f"Passo de Euler com {num_subintervalos} subintervalos (h = {passo_h}):")
    print(f"y(0) = {temp_inicial:.6f}°C")
    
    for i in range(num_subintervalos):
        tempo = valores_tempo[i]
        temperatura = valores_temperatura[i]
        valor_f = f(temperatura, temp_ambiente, constante_k)
        temperatura_proxima = temperatura + passo_h * valor_f
        valores_temperatura[i + 1] = temperatura_proxima
        
        print(f"Passo {i+1}:")
        print(f"t_{i} = {tempo:.6f}, y_{i} = {temperatura:.6f}, f(y_{i}) = {valor_f:.6f}")
        print(f"y_{i+1} = y_{i} + h * f(y_{i}) = {temperatura:.6f} + {passo_h:.6f} * {valor_f:.6f} = {temperatura_proxima:.6f}")
        print("-" * 50)
    
    return valores_tempo, valores_temperatura

temp_inicial = 42
temp_ambiente = 25
constante_k = 2
tempo_final = 3
num_subintervalos = 100

valores_tempo, valores_temperatura = metodo_euler(temp_inicial, temp_ambiente, constante_k, tempo_final, num_subintervalos)

print(f"\nTemperatura após {tempo_final} horas: {valores_temperatura[-1]:.6f}°C")