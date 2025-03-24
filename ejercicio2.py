import time
import matplotlib.pyplot as plt
import numpy as np

# Función de la Torre de Hanoi basada en la imagen
def towersOfHanoi(nro_disks, _from=1, _to=3, _tmp=2):
    if nro_disks == 1:
        return
    
    towersOfHanoi(nro_disks - 1, _from, _tmp, _to)
    towersOfHanoi(nro_disks - 1, _tmp, _to, _from)

# Lista de valores de discos
n_values = np.arange(1, 15)  # Número de discos de 1 a 14
times = []  # Lista para almacenar los tiempos

# Medir el tiempo de ejecución para cada n
for n in n_values:
    start_time = time.time()  # Iniciar cronómetro
    towersOfHanoi(n)  # Ejecutar la función
    end_time = time.time()  # Terminar cronómetro
    times.append(end_time - start_time)  # Guardar tiempo transcurrido

# Graficar los tiempos de ejecución
plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', color='r', label="Tiempo de ejecución")
plt.xlabel("Número de Discos")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de Resolución de la Torre de Hanoi")
plt.yscale("log")  # Escala logarítmica para mejor visualización
plt.grid(True)
plt.legend()
plt.show()