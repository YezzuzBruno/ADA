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
    for i in range (0, n, 100):
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

def generar_arreglos_average_case(n):
    result = []
    for i in range(1,n+1):
        lista = []
        for j in range(0, i):
            lista.append(random.randint(1,n))
        result.append(lista)
    return result

def calcular_tiempos(arreglo):
    tiempos = []
    for i in arreglo:
        inicio = time.time()
        insertion_sort(i)
        fin = time.time()
        tiempos.append(fin-inicio)
    return tiempos

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

def generar_diagrama_total(sizes, average_case_times, best_case_times,worst_case_times):
    # Crear el gráfico
    plt.plot(sizes, average_case_times, marker='o', color='blue', label='Caso promedio')
    plt.plot(sizes, best_case_times, marker='o', color='green', label='Mejor caso')
    plt.plot(sizes, worst_case_times, marker='o', color='red', label='Peor caso')

    plt.title("Tiempos de ejecución de Insertion Sort")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    n = sys.argv[1]
    #generar los arrays de tamaños recibidos por el computador
    
    arreglos_peor_caso = generar_arreglos_worst_case(int(n))
    #arreglos_mejor_caso =  generar_arreglos_best_case(int(n))
    #arreglos_caso_promedio = generar_arreglos_average_case(int(n))

    sizes = list(range(100, int(n)+1, 100))
    
    #average_case_times = calcular_tiempos(arreglos_caso_promedio)
    #best_case_times = calcular_tiempos(arreglos_mejor_caso)
    worst_case_times = calcular_tiempos(arreglos_peor_caso)
    print(len(sizes))
    print(len(worst_case_times))
    generar_diagrama(sizes, worst_case_times)
    #generar_diagrama_total(sizes, average_case_times, best_case_times, worst_case_times)
