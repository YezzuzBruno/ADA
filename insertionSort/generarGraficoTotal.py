import sys
import json
import matplotlib.pyplot as plt

def generar_diagrama():
    plt.figure(figsize=(12,6))
    
    for line in sys.stdin:
        if line.strip():
            datos = json.loads(line)
            if datos["tipo"] == "Mejor Caso":
                plt.plot(datos["sizes"], datos["times"], 'g-', label='Mejor Caso (Ordenado)')
            elif datos["tipo"] == "Peor Caso":
                plt.plot(datos["sizes"], datos["times"], 'r-', label='Peor Caso (Invertido)')
    
    plt.title("Tiempos de ejecución de Insertion Sort")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    generar_diagrama()
