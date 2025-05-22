import time
import sys
import json

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def calcular_tiempos():
    for linea in sys.stdin:
        arreglo = json.loads(linea)
        inicio = time.time()
        insertion_sort(arreglo)
        fin = time.time()
        tiempo = fin - inicio
        print(json.dumps({
            "tam" : len(arreglo),
            "time" : tiempo
        }))


if __name__ == "__main__":
    calcular_tiempos()
