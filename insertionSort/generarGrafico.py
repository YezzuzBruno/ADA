import sys
import json
import matplotlib.pyplot as plt

sizes = []
times = []
for line in sys.stdin:
    if line.strip():  # evitar líneas vacías
        datos = json.loads(line)
        sizes.append(datos["tam"])
        times.append(datos["time"])


def generar_diagrama(sizes, times):
    # Gráfico
    plt.figure(figsize=(12,6))
    plt.plot(sizes, times, color='blue', label='Insertion Sort')
    plt.title("Tiempos de ejecución de Insertion Sort")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    generar_diagrama(sizes, times)
