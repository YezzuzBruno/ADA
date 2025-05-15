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
    print(n)
    result = []
    for i in range (0, n):
        lista = []
        for j in range(i,-1,-1):
            lista.append(j+1)
        result.append(lista)
    return result

if __name__ == "__main__":
    n = sys.argv[1]
    #generar los arrays de tamaños recibidos por el computador
    arreglos = generar_arreglos_worst_case(int(n))
    tiempos = []
    print(arreglos)
    for i in arreglos:
        inicio = time.time()
        insertion_sort(i)
        fin = time.time()
        tiempos.append(fin-inicio)
    #insertion_sort(numbers_worst_case)
    print("Arreglados \n:")
    print(arreglos)
    print("Tiempos tomado para ordenar cada arreglo: \n")
    for t in tiempos:
        print(f"{t:.10f}")
