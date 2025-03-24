# Factorial function using recursion
import sys

sys.setrecursionlimit(5000)  # Aumenta el límite a 5000 (ajústalo según necesidad)

import time
import matplotlib.pyplot as plt

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Measure execution time for different inputs
values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 2080, 2100, 4096]
times = []

for val in values:
    start_time = time.time()
    factorial(val)
    end_time = time.time()
    times.append(end_time - start_time)

# Plotting results
plt.plot(values, times, marker='o', linestyle='-')
plt.xlabel("Input Value (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Factorial Execution Time Analysis")
plt.grid(True)
plt.show()