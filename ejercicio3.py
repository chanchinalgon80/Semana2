import time
import matplotlib.pyplot as plt

# Función recursiva para generar combinaciones binarias
def generate_binary_strings(n, result=""):
    if len(result) == n:
        return [result]  # Devuelve la combinación en una lista
    return (generate_binary_strings(n, result + '0') + 
            generate_binary_strings(n, result + '1'))

# Función para medir el tiempo de ejecución y devolver los resultados
def measure_time(n):
    start_time = time.time()
    combinations = generate_binary_strings(n)
    end_time = time.time()
    return combinations, end_time - start_time

# Función para calcular el número de permutaciones binarias
def count_permutations(n):
    return 2 ** n  # Fórmula: 2^n combinaciones posibles

if __name__ == "__main__":
    # Valores de n a evaluar
    bit_values = [3, 4, 5, 6]
    times = []

    # Iterar sobre cada valor de n, calcular permutaciones y medir tiempo
    for n in bit_values:
        _, execution_time = measure_time(n)
        times.append(execution_time)
    
    # Graficar los tiempos de ejecución
    plt.figure(figsize=(8, 5))
    plt.plot(bit_values, times, marker='o', linestyle='-', color='blue', label="Execution Time")
    plt.xlabel("Number of Bits")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time for Binary Combinations Generation")
    plt.legend()
    plt.grid(True)
    plt.show()