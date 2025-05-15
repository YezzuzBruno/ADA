import time
import matplotlib.pyplot as plt
import random
import sys

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generar_arreglos_worst_case(n):
    result = []
    for i in range (0, n):
        lista = []
        for j in range(i,-1,-1):
            lista.append(j+1)
        result.append(lista)
    return result

def generar_arreglos_best_case(n):
    result = []
    for i in range (1, n+1):
        lista = []
        for j in range(1, i+1):
            lista.append(j)
        result.append(lista)
    return result

def generar_diagrama(sizes, times):
    # Gráfico
    plt.plot(sizes, times, marker='o', color='blue', label='Insertion Sort')
    plt.title("Tiempos de ejecución de Insertion Sort")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    n = sys.argv[1]
    #generar los arrays de tamaños recibidos por el computador
    #arreglos_peor_caso = generar_arreglos_worst_case(int(n))
    arreglos_mejor_caso =  generar_arreglos_best_case(int(n))
    tiempos = []
    sizes = []
    total_time = 0
    for i in arreglos_mejor_caso:
        inicio = time.time()
        insertion_sort(i)
        fin = time.time()
        tiempos.append(fin-inicio)
        sizes.append(len(i))
        total_time+=(fin-inicio)
    print(total_time)
    print(tiempos)
    generar_diagrama(sizes, tiempos)
